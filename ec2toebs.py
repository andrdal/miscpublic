#!/usr/bin/env python3

#Sync EC2 Tag Name with EBS Tag Name

import boto3
ec2 = boto3.resource('ec2')

print ("Loop for TAG Name")
for volume in ec2.volumes.all():
  print(volume.id)
  for attachment in volume.attachments:
    print(attachment['InstanceId'])
    for name in ec2.Instance(attachment['InstanceId']).tags:
        if name['Key'] == 'Name':
          tag = volume.create_tags(
            DryRun=False,
            Resources=[volume.id],
            Tags=[{'Key':'Name','Value':name['Value']}]
)

#Sync EC2 Tag Project with EBS Tag Project

print ("Loop for TAG Project")
for volume in ec2.volumes.all():
  print(volume.id)
  for attachment in volume.attachments:
    print(attachment['InstanceId'])
    for name in ec2.Instance(attachment['InstanceId']).tags:
      if name['Key'] == 'Project':
          tag = volume.create_tags(
          DryRun=False,
          Resources=[volume.id],
          Tags=[{'Key':'Project','Value':name['Value']}]
)