#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB including top 10 IPs
"""
from pymongo import MongoClient


def log_stats():
    """
    Prints stats about Nginx logs including top IPs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check_count))

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_collection.aggregate(pipeline)
    for ip_data in top_ips:
        print("\t{}: {}".format(ip_data.get('_id'), ip_data.get('count')))


if __name__ == "__main__":
    log_stats()
