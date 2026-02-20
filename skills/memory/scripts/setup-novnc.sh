#!/bin/bash
# setup-novnc.sh - Helper script to manage noVNC display services
# Run this if you need to manually restart the display stack

set -e

echo "=== noVNC Setup Helper ==="

# Check if running as ubuntu user
if [ "$USER" != "ubuntu" ]; then
    echo "This script should be run as the ubuntu user"
    exit 1
fi

case "${1:-status}" in
    start)
        echo "Starting display services..."
        sudo systemctl start xvfb
        sleep 2
        sudo systemctl start fluxbox
        sleep 1
        sudo systemctl start x11vnc
        sleep 1
        sudo systemctl start novnc
        echo "Display services started!"
        echo "Access noVNC at: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4):6080"
        ;;

    stop)
        echo "Stopping display services..."
        sudo systemctl stop novnc x11vnc fluxbox xvfb || true
        echo "Display services stopped"
        ;;

    restart)
        $0 stop
        sleep 2
        $0 start
        ;;

    status)
        echo "Display service status:"
        echo ""
        for service in xvfb fluxbox x11vnc novnc; do
            status=$(systemctl is-active $service 2>/dev/null || echo "inactive")
            printf "  %-12s %s\n" "$service:" "$status"
        done
        echo ""
        if systemctl is-active --quiet novnc; then
            PUBLIC_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null || echo "unknown")
            echo "noVNC URL: http://$PUBLIC_IP:6080"
        fi
        ;;

    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
