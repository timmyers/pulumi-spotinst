// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package multai

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Spotinst Multai Target Set.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/multai_target_set.html.markdown.
type TargetSet struct {
	s *pulumi.ResourceState
}

// NewTargetSet registers a new resource with the given unique name, arguments, and options.
func NewTargetSet(ctx *pulumi.Context,
	name string, args *TargetSetArgs, opts ...pulumi.ResourceOpt) (*TargetSet, error) {
	if args == nil || args.BalancerId == nil {
		return nil, errors.New("missing required argument 'BalancerId'")
	}
	if args == nil || args.DeploymentId == nil {
		return nil, errors.New("missing required argument 'DeploymentId'")
	}
	if args == nil || args.HealthCheck == nil {
		return nil, errors.New("missing required argument 'HealthCheck'")
	}
	if args == nil || args.Protocol == nil {
		return nil, errors.New("missing required argument 'Protocol'")
	}
	if args == nil || args.Weight == nil {
		return nil, errors.New("missing required argument 'Weight'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["balancerId"] = nil
		inputs["deploymentId"] = nil
		inputs["healthCheck"] = nil
		inputs["name"] = nil
		inputs["port"] = nil
		inputs["protocol"] = nil
		inputs["tags"] = nil
		inputs["weight"] = nil
	} else {
		inputs["balancerId"] = args.BalancerId
		inputs["deploymentId"] = args.DeploymentId
		inputs["healthCheck"] = args.HealthCheck
		inputs["name"] = args.Name
		inputs["port"] = args.Port
		inputs["protocol"] = args.Protocol
		inputs["tags"] = args.Tags
		inputs["weight"] = args.Weight
	}
	s, err := ctx.RegisterResource("spotinst:multai/targetSet:TargetSet", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TargetSet{s: s}, nil
}

// GetTargetSet gets an existing TargetSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTargetSet(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TargetSetState, opts ...pulumi.ResourceOpt) (*TargetSet, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["balancerId"] = state.BalancerId
		inputs["deploymentId"] = state.DeploymentId
		inputs["healthCheck"] = state.HealthCheck
		inputs["name"] = state.Name
		inputs["port"] = state.Port
		inputs["protocol"] = state.Protocol
		inputs["tags"] = state.Tags
		inputs["weight"] = state.Weight
	}
	s, err := ctx.ReadResource("spotinst:multai/targetSet:TargetSet", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TargetSet{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *TargetSet) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *TargetSet) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The id of the balancer.
func (r *TargetSet) BalancerId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["balancerId"])
}

// The id of the deployment.
func (r *TargetSet) DeploymentId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["deploymentId"])
}

func (r *TargetSet) HealthCheck() *pulumi.Output {
	return r.s.State["healthCheck"]
}

// The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
func (r *TargetSet) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The port on which the load balancer is listening.
func (r *TargetSet) Port() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["port"])
}

// The protocol to allow connections to the target for the health check.
func (r *TargetSet) Protocol() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["protocol"])
}

// A list of key:value paired tags.
func (r *TargetSet) Tags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["tags"])
}

// Defines how traffic is distributed between the Target Set.
func (r *TargetSet) Weight() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["weight"])
}

// Input properties used for looking up and filtering TargetSet resources.
type TargetSetState struct {
	// The id of the balancer.
	BalancerId interface{}
	// The id of the deployment.
	DeploymentId interface{}
	HealthCheck interface{}
	// The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
	Name interface{}
	// The port on which the load balancer is listening.
	Port interface{}
	// The protocol to allow connections to the target for the health check.
	Protocol interface{}
	// A list of key:value paired tags.
	Tags interface{}
	// Defines how traffic is distributed between the Target Set.
	Weight interface{}
}

// The set of arguments for constructing a TargetSet resource.
type TargetSetArgs struct {
	// The id of the balancer.
	BalancerId interface{}
	// The id of the deployment.
	DeploymentId interface{}
	HealthCheck interface{}
	// The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
	Name interface{}
	// The port on which the load balancer is listening.
	Port interface{}
	// The protocol to allow connections to the target for the health check.
	Protocol interface{}
	// A list of key:value paired tags.
	Tags interface{}
	// Defines how traffic is distributed between the Target Set.
	Weight interface{}
}
