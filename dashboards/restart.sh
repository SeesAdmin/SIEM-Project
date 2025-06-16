#!/bin/bash
echo "Stack Restart" | tee -a restart.log
echo "$(date)" | tee -a restart.log

echo "Elasticsearch Restart"
sudo systemctl restart elasticsearch

echo "Kibana Restart"
sudo systemctl restart kibana

echo "AlertBot Restart"
sudo systemctl restart alertbot

echo "All services have been restarted" | tee -a restart.log
