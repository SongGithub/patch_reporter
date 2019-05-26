"""
patch-reporter - ec2_instance_queries
~~~~~~~~~~~~~~
This module provides utility to query ec2 instances within account
and output tags in list of dicts format [dict1, dict2, ... ,dictn]
"""
import boto3


def list_instance_by_tags(tag_key,tag_value):
    '''return filtered instances with specified tag-value combination'''
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
    ''' given an instance, list all its tags'''
    pass

def convert_tags_to_dict(tag_list):
    '''
        given a list of tags in AWS format,
        return well-formatted dict {key1: val1, key2: val2}
        input: [
                {'Key': 'key2', 'Value': 'val2'},
                {'Key': 'key1', 'Value': 'val1'}
            ]
        output: {key1: val1, key2: val2}
    '''
    pass

if __name__ == '__main__':
    found_instances = list_instance_by_tags(tag_key='CostCentre', tag_value='V_ABC')
    print(found_instances['InstanceId'], found_instances['ImageId'])