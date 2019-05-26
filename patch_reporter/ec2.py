# -*- coding: utf-8 -*-

"""
patch-reporter - ec2_instance_queries
~~~~~~~~~~~~~~
This module provides utility to query ec2 instances within account
"""
import boto3

def convert_tags_to_dict(tag_list):
    '''
        input: [{'Key': 'key2', 'Value': 'val2'}, {'Key': 'key1', 'Value': 'val1'}]
        output: {key1: val1, key2: val2}
    '''


def list_instance_by_tags(tag_key,tag_value):
    '''return instances with input tag-value combination'''
    ec2 = boto3.client("ec2", region_name = 'ap-southeast-2')
    reservations = ec2.describe_instances()['Reservations']
    instances = []
    for reservation in reservations:
        for instance in reservation['Instances']:
            for tag in instance['Tags']:
                if tag['Key'] == tag_key and tag['Value'] == tag_value:
                    instances.append(instance)
    return instances

def list_instance_tags(instance):
    ''' given an instance, list all tags'''
    pass


found_instances = list_instance_by_tags(tag_key='CostCentre', tag_value='V_ABC')
print(found_instances['InstanceId'], found_instances['ImageId'])