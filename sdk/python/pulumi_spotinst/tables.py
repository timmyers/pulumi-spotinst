# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

_SNAKE_TO_CAMEL_CASE_TABLE = {
    "additional_info": "additionalInfo",
    "additional_primary_security_groups": "additionalPrimarySecurityGroups",
    "additional_replica_security_groups": "additionalReplicaSecurityGroups",
    "associate_public_ip_address": "associatePublicIpAddress",
    "auto_healing": "autoHealing",
    "availability_zones": "availabilityZones",
    "backend_services": "backendServices",
    "balancer_id": "balancerId",
    "beanstalk_environment_id": "beanstalkEnvironmentId",
    "beanstalk_environment_name": "beanstalkEnvironmentName",
    "block_devices_mode": "blockDevicesMode",
    "bootstrap_actions_files": "bootstrapActionsFiles",
    "capacity_unit": "capacityUnit",
    "cluster_controller_id": "clusterControllerId",
    "cluster_id": "clusterId",
    "cluster_name": "clusterName",
    "cluster_zone_name": "clusterZoneName",
    "configurations_files": "configurationsFiles",
    "connection_timeouts": "connectionTimeouts",
    "controller_id": "controllerId",
    "core_desired_capacity": "coreDesiredCapacity",
    "core_ebs_block_devices": "coreEbsBlockDevices",
    "core_ebs_optimized": "coreEbsOptimized",
    "core_instance_types": "coreInstanceTypes",
    "core_lifecycle": "coreLifecycle",
    "core_max_size": "coreMaxSize",
    "core_min_size": "coreMinSize",
    "core_scaling_down_policies": "coreScalingDownPolicies",
    "core_scaling_up_policies": "coreScalingUpPolicies",
    "cpu_credits": "cpuCredits",
    "custom_ami_id": "customAmiId",
    "custom_data": "customData",
    "deployment_id": "deploymentId",
    "deployment_preferences": "deploymentPreferences",
    "desired_capacity": "desiredCapacity",
    "dns_cname_aliases": "dnsCnameAliases",
    "draining_timeout": "drainingTimeout",
    "ebs_block_devices": "ebsBlockDevices",
    "ebs_optimized": "ebsOptimized",
    "ebs_root_volume_size": "ebsRootVolumeSize",
    "ec2_key_name": "ec2KeyName",
    "elastic_ips": "elasticIps",
    "elastic_load_balancers": "elasticLoadBalancers",
    "enable_monitoring": "enableMonitoring",
    "ephemeral_block_devices": "ephemeralBlockDevices",
    "event_type": "eventType",
    "expose_cluster_id": "exposeClusterId",
    "fallback_to_ondemand": "fallbackToOndemand",
    "health_check": "healthCheck",
    "health_check_grace_period": "healthCheckGracePeriod",
    "health_check_type": "healthCheckType",
    "health_check_unhealthy_duration_before_replacement": "healthCheckUnhealthyDurationBeforeReplacement",
    "iam_instance_profile": "iamInstanceProfile",
    "image_id": "imageId",
    "instance_types_customs": "instanceTypesCustoms",
    "instance_types_ondemand": "instanceTypesOndemand",
    "instance_types_preemptibles": "instanceTypesPreemptibles",
    "instance_types_preferred_spots": "instanceTypesPreferredSpots",
    "instance_types_spots": "instanceTypesSpots",
    "instance_types_weights": "instanceTypesWeights",
    "instance_weights": "instanceWeights",
    "integration_beanstalk": "integrationBeanstalk",
    "integration_codedeploy": "integrationCodedeploy",
    "integration_docker_swarm": "integrationDockerSwarm",
    "integration_ecs": "integrationEcs",
    "integration_gitlab": "integrationGitlab",
    "integration_gke": "integrationGke",
    "integration_kubernetes": "integrationKubernetes",
    "integration_mesosphere": "integrationMesosphere",
    "integration_multai_runtime": "integrationMultaiRuntime",
    "integration_nomad": "integrationNomad",
    "integration_rancher": "integrationRancher",
    "integration_route53": "integrationRoute53",
    "ip_forwarding": "ipForwarding",
    "job_flow_role": "jobFlowRole",
    "keep_job_flow_alive": "keepJobFlowAlive",
    "key_name": "keyName",
    "key_pair": "keyPair",
    "lifetime_period": "lifetimePeriod",
    "listener_id": "listenerId",
    "load_balancers": "loadBalancers",
    "log_uri": "logUri",
    "low_priority_sizes": "lowPrioritySizes",
    "managed_actions": "managedActions",
    "managed_primary_security_group": "managedPrimarySecurityGroup",
    "managed_replica_security_group": "managedReplicaSecurityGroup",
    "managed_service_identities": "managedServiceIdentities",
    "master_ebs_block_devices": "masterEbsBlockDevices",
    "master_ebs_optimized": "masterEbsOptimized",
    "master_instance_types": "masterInstanceTypes",
    "master_lifecycle": "masterLifecycle",
    "max_size": "maxSize",
    "middleware_ids": "middlewareIds",
    "min_size": "minSize",
    "multai_target_sets": "multaiTargetSets",
    "network_interfaces": "networkInterfaces",
    "node_image": "nodeImage",
    "node_pool_name": "nodePoolName",
    "ocean_id": "oceanId",
    "od_sizes": "odSizes",
    "ondemand_count": "ondemandCount",
    "output_cluster_id": "outputClusterId",
    "persist_block_devices": "persistBlockDevices",
    "persist_private_ip": "persistPrivateIp",
    "persist_root_device": "persistRootDevice",
    "placement_tenancy": "placementTenancy",
    "preemptible_percentage": "preemptiblePercentage",
    "preferred_availability_zones": "preferredAvailabilityZones",
    "private_ips": "privateIps",
    "provisioning_timeout": "provisioningTimeout",
    "release_label": "releaseLabel",
    "repo_upgrade_on_boot": "repoUpgradeOnBoot",
    "resource_group_name": "resourceGroupName",
    "resource_id": "resourceId",
    "revert_to_spot": "revertToSpot",
    "root_volume_size": "rootVolumeSize",
    "scaling_down_policies": "scalingDownPolicies",
    "scaling_strategies": "scalingStrategies",
    "scaling_target_policies": "scalingTargetPolicies",
    "scaling_up_policies": "scalingUpPolicies",
    "scheduled_tasks": "scheduledTasks",
    "security_config": "securityConfig",
    "security_group_ids": "securityGroupIds",
    "security_groups": "securityGroups",
    "service_access_security_group": "serviceAccessSecurityGroup",
    "service_account": "serviceAccount",
    "service_role": "serviceRole",
    "shutdown_script": "shutdownScript",
    "source_image": "sourceImage",
    "spot_percentage": "spotPercentage",
    "startup_script": "startupScript",
    "stateful_deallocation": "statefulDeallocation",
    "steps_files": "stepsFiles",
    "subnet_ids": "subnetIds",
    "target_group_arns": "targetGroupArns",
    "target_set_id": "targetSetId",
    "target_set_ids": "targetSetIds",
    "task_desired_capacity": "taskDesiredCapacity",
    "task_ebs_block_devices": "taskEbsBlockDevices",
    "task_ebs_optimized": "taskEbsOptimized",
    "task_instance_types": "taskInstanceTypes",
    "task_lifecycle": "taskLifecycle",
    "task_max_size": "taskMaxSize",
    "task_min_size": "taskMinSize",
    "task_scaling_down_policies": "taskScalingDownPolicies",
    "task_scaling_up_policies": "taskScalingUpPolicies",
    "termination_protected": "terminationProtected",
    "tls_config": "tlsConfig",
    "unhealthy_duration": "unhealthyDuration",
    "update_policy": "updatePolicy",
    "user_data": "userData",
    "utilize_reserved_instances": "utilizeReservedInstances",
    "visible_to_all_users": "visibleToAllUsers",
    "wait_for_capacity": "waitForCapacity",
    "wait_for_capacity_timeout": "waitForCapacityTimeout",
}

_CAMEL_TO_SNAKE_CASE_TABLE = {
    "additionalInfo": "additional_info",
    "additionalPrimarySecurityGroups": "additional_primary_security_groups",
    "additionalReplicaSecurityGroups": "additional_replica_security_groups",
    "associatePublicIpAddress": "associate_public_ip_address",
    "autoHealing": "auto_healing",
    "availabilityZones": "availability_zones",
    "backendServices": "backend_services",
    "balancerId": "balancer_id",
    "beanstalkEnvironmentId": "beanstalk_environment_id",
    "beanstalkEnvironmentName": "beanstalk_environment_name",
    "blockDevicesMode": "block_devices_mode",
    "bootstrapActionsFiles": "bootstrap_actions_files",
    "capacityUnit": "capacity_unit",
    "clusterControllerId": "cluster_controller_id",
    "clusterId": "cluster_id",
    "clusterName": "cluster_name",
    "clusterZoneName": "cluster_zone_name",
    "configurationsFiles": "configurations_files",
    "connectionTimeouts": "connection_timeouts",
    "controllerId": "controller_id",
    "coreDesiredCapacity": "core_desired_capacity",
    "coreEbsBlockDevices": "core_ebs_block_devices",
    "coreEbsOptimized": "core_ebs_optimized",
    "coreInstanceTypes": "core_instance_types",
    "coreLifecycle": "core_lifecycle",
    "coreMaxSize": "core_max_size",
    "coreMinSize": "core_min_size",
    "coreScalingDownPolicies": "core_scaling_down_policies",
    "coreScalingUpPolicies": "core_scaling_up_policies",
    "cpuCredits": "cpu_credits",
    "customAmiId": "custom_ami_id",
    "customData": "custom_data",
    "deploymentId": "deployment_id",
    "deploymentPreferences": "deployment_preferences",
    "desiredCapacity": "desired_capacity",
    "dnsCnameAliases": "dns_cname_aliases",
    "drainingTimeout": "draining_timeout",
    "ebsBlockDevices": "ebs_block_devices",
    "ebsOptimized": "ebs_optimized",
    "ebsRootVolumeSize": "ebs_root_volume_size",
    "ec2KeyName": "ec2_key_name",
    "elasticIps": "elastic_ips",
    "elasticLoadBalancers": "elastic_load_balancers",
    "enableMonitoring": "enable_monitoring",
    "ephemeralBlockDevices": "ephemeral_block_devices",
    "eventType": "event_type",
    "exposeClusterId": "expose_cluster_id",
    "fallbackToOndemand": "fallback_to_ondemand",
    "healthCheck": "health_check",
    "healthCheckGracePeriod": "health_check_grace_period",
    "healthCheckType": "health_check_type",
    "healthCheckUnhealthyDurationBeforeReplacement": "health_check_unhealthy_duration_before_replacement",
    "iamInstanceProfile": "iam_instance_profile",
    "imageId": "image_id",
    "instanceTypesCustoms": "instance_types_customs",
    "instanceTypesOndemand": "instance_types_ondemand",
    "instanceTypesPreemptibles": "instance_types_preemptibles",
    "instanceTypesPreferredSpots": "instance_types_preferred_spots",
    "instanceTypesSpots": "instance_types_spots",
    "instanceTypesWeights": "instance_types_weights",
    "instanceWeights": "instance_weights",
    "integrationBeanstalk": "integration_beanstalk",
    "integrationCodedeploy": "integration_codedeploy",
    "integrationDockerSwarm": "integration_docker_swarm",
    "integrationEcs": "integration_ecs",
    "integrationGitlab": "integration_gitlab",
    "integrationGke": "integration_gke",
    "integrationKubernetes": "integration_kubernetes",
    "integrationMesosphere": "integration_mesosphere",
    "integrationMultaiRuntime": "integration_multai_runtime",
    "integrationNomad": "integration_nomad",
    "integrationRancher": "integration_rancher",
    "integrationRoute53": "integration_route53",
    "ipForwarding": "ip_forwarding",
    "jobFlowRole": "job_flow_role",
    "keepJobFlowAlive": "keep_job_flow_alive",
    "keyName": "key_name",
    "keyPair": "key_pair",
    "lifetimePeriod": "lifetime_period",
    "listenerId": "listener_id",
    "loadBalancers": "load_balancers",
    "logUri": "log_uri",
    "lowPrioritySizes": "low_priority_sizes",
    "managedActions": "managed_actions",
    "managedPrimarySecurityGroup": "managed_primary_security_group",
    "managedReplicaSecurityGroup": "managed_replica_security_group",
    "managedServiceIdentities": "managed_service_identities",
    "masterEbsBlockDevices": "master_ebs_block_devices",
    "masterEbsOptimized": "master_ebs_optimized",
    "masterInstanceTypes": "master_instance_types",
    "masterLifecycle": "master_lifecycle",
    "maxSize": "max_size",
    "middlewareIds": "middleware_ids",
    "minSize": "min_size",
    "multaiTargetSets": "multai_target_sets",
    "networkInterfaces": "network_interfaces",
    "nodeImage": "node_image",
    "nodePoolName": "node_pool_name",
    "oceanId": "ocean_id",
    "odSizes": "od_sizes",
    "ondemandCount": "ondemand_count",
    "outputClusterId": "output_cluster_id",
    "persistBlockDevices": "persist_block_devices",
    "persistPrivateIp": "persist_private_ip",
    "persistRootDevice": "persist_root_device",
    "placementTenancy": "placement_tenancy",
    "preemptiblePercentage": "preemptible_percentage",
    "preferredAvailabilityZones": "preferred_availability_zones",
    "privateIps": "private_ips",
    "provisioningTimeout": "provisioning_timeout",
    "releaseLabel": "release_label",
    "repoUpgradeOnBoot": "repo_upgrade_on_boot",
    "resourceGroupName": "resource_group_name",
    "resourceId": "resource_id",
    "revertToSpot": "revert_to_spot",
    "rootVolumeSize": "root_volume_size",
    "scalingDownPolicies": "scaling_down_policies",
    "scalingStrategies": "scaling_strategies",
    "scalingTargetPolicies": "scaling_target_policies",
    "scalingUpPolicies": "scaling_up_policies",
    "scheduledTasks": "scheduled_tasks",
    "securityConfig": "security_config",
    "securityGroupIds": "security_group_ids",
    "securityGroups": "security_groups",
    "serviceAccessSecurityGroup": "service_access_security_group",
    "serviceAccount": "service_account",
    "serviceRole": "service_role",
    "shutdownScript": "shutdown_script",
    "sourceImage": "source_image",
    "spotPercentage": "spot_percentage",
    "startupScript": "startup_script",
    "statefulDeallocation": "stateful_deallocation",
    "stepsFiles": "steps_files",
    "subnetIds": "subnet_ids",
    "targetGroupArns": "target_group_arns",
    "targetSetId": "target_set_id",
    "targetSetIds": "target_set_ids",
    "taskDesiredCapacity": "task_desired_capacity",
    "taskEbsBlockDevices": "task_ebs_block_devices",
    "taskEbsOptimized": "task_ebs_optimized",
    "taskInstanceTypes": "task_instance_types",
    "taskLifecycle": "task_lifecycle",
    "taskMaxSize": "task_max_size",
    "taskMinSize": "task_min_size",
    "taskScalingDownPolicies": "task_scaling_down_policies",
    "taskScalingUpPolicies": "task_scaling_up_policies",
    "terminationProtected": "termination_protected",
    "tlsConfig": "tls_config",
    "unhealthyDuration": "unhealthy_duration",
    "updatePolicy": "update_policy",
    "userData": "user_data",
    "utilizeReservedInstances": "utilize_reserved_instances",
    "visibleToAllUsers": "visible_to_all_users",
    "waitForCapacity": "wait_for_capacity",
    "waitForCapacityTimeout": "wait_for_capacity_timeout",
}
