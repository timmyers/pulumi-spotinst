# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class TargetSet(pulumi.CustomResource):
    balancer_id: pulumi.Output[str]
    """
    The id of the balancer.
    """
    deployment_id: pulumi.Output[str]
    """
    The id of the deployment.
    """
    health_check: pulumi.Output[dict]
    name: pulumi.Output[str]
    """
    The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
    """
    port: pulumi.Output[float]
    """
    The port on which the load balancer is listening.
    """
    protocol: pulumi.Output[str]
    """
    The protocol to allow connections to the target for the health check.
    """
    tags: pulumi.Output[list]
    """
    A list of key:value paired tags.
    
      * `key` (`str`) - The tag's key.
      * `value` (`str`) - The tag's value.
    """
    weight: pulumi.Output[float]
    """
    Defines how traffic is distributed between the Target Set.
    """
    def __init__(__self__, resource_name, opts=None, balancer_id=None, deployment_id=None, health_check=None, name=None, port=None, protocol=None, tags=None, weight=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Spotinst Multai Target Set.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] balancer_id: The id of the balancer.
        :param pulumi.Input[str] deployment_id: The id of the deployment.
        :param pulumi.Input[str] name: The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
        :param pulumi.Input[float] port: The port on which the load balancer is listening.
        :param pulumi.Input[str] protocol: The protocol to allow connections to the target for the health check.
        :param pulumi.Input[list] tags: A list of key:value paired tags.
        :param pulumi.Input[float] weight: Defines how traffic is distributed between the Target Set.
        
        The **health_check** object supports the following:
        
          * `healthyThreshold` (`pulumi.Input[float]`) - Total number of allowed healthy Targets.
          * `interval` (`pulumi.Input[float]`) - The interval for the health check.
          * `path` (`pulumi.Input[str]`) - The path to perform the health check.
          * `port` (`pulumi.Input[float]`) - The port on which the load balancer is listening.
          * `protocol` (`pulumi.Input[str]`) - The protocol to allow connections to the target for the health check.
          * `timeout` (`pulumi.Input[float]`) - The time out for the health check.
          * `unhealthyThreshold` (`pulumi.Input[float]`) - Total number of allowed unhealthy Targets.
        
        The **tags** object supports the following:
        
          * `key` (`pulumi.Input[str]`) - The tag's key.
          * `value` (`pulumi.Input[str]`) - The tag's value.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/multai_target_set.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if balancer_id is None:
                raise TypeError("Missing required property 'balancer_id'")
            __props__['balancer_id'] = balancer_id
            if deployment_id is None:
                raise TypeError("Missing required property 'deployment_id'")
            __props__['deployment_id'] = deployment_id
            if health_check is None:
                raise TypeError("Missing required property 'health_check'")
            __props__['health_check'] = health_check
            __props__['name'] = name
            __props__['port'] = port
            if protocol is None:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            __props__['tags'] = tags
            if weight is None:
                raise TypeError("Missing required property 'weight'")
            __props__['weight'] = weight
        super(TargetSet, __self__).__init__(
            'spotinst:multai/targetSet:TargetSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, balancer_id=None, deployment_id=None, health_check=None, name=None, port=None, protocol=None, tags=None, weight=None):
        """
        Get an existing TargetSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] balancer_id: The id of the balancer.
        :param pulumi.Input[str] deployment_id: The id of the deployment.
        :param pulumi.Input[str] name: The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
        :param pulumi.Input[float] port: The port on which the load balancer is listening.
        :param pulumi.Input[str] protocol: The protocol to allow connections to the target for the health check.
        :param pulumi.Input[list] tags: A list of key:value paired tags.
        :param pulumi.Input[float] weight: Defines how traffic is distributed between the Target Set.
        
        The **health_check** object supports the following:
        
          * `healthyThreshold` (`pulumi.Input[float]`) - Total number of allowed healthy Targets.
          * `interval` (`pulumi.Input[float]`) - The interval for the health check.
          * `path` (`pulumi.Input[str]`) - The path to perform the health check.
          * `port` (`pulumi.Input[float]`) - The port on which the load balancer is listening.
          * `protocol` (`pulumi.Input[str]`) - The protocol to allow connections to the target for the health check.
          * `timeout` (`pulumi.Input[float]`) - The time out for the health check.
          * `unhealthyThreshold` (`pulumi.Input[float]`) - Total number of allowed unhealthy Targets.
        
        The **tags** object supports the following:
        
          * `key` (`pulumi.Input[str]`) - The tag's key.
          * `value` (`pulumi.Input[str]`) - The tag's value.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/multai_target_set.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["balancer_id"] = balancer_id
        __props__["deployment_id"] = deployment_id
        __props__["health_check"] = health_check
        __props__["name"] = name
        __props__["port"] = port
        __props__["protocol"] = protocol
        __props__["tags"] = tags
        __props__["weight"] = weight
        return TargetSet(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

