// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package spotinst

import (
	"unicode"

	"github.com/hashicorp/terraform/helper/schema"
	"github.com/hashicorp/terraform/terraform"
	"github.com/pulumi/pulumi-terraform/pkg/tfbridge"
	"github.com/pulumi/pulumi/pkg/resource"
	"github.com/pulumi/pulumi/pkg/tokens"
	"github.com/terraform-providers/terraform-provider-spotinst/spotinst"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "spotinst"
	// modules:
	awsMod          = "aws"
	ecsMod          = "ecs"
	gcpMod          = "gcp"
	gkeMod          = "gke"
	azureMod        = "azure"
	multaiMod       = "multai"
	subscriptionMod = "index"
)

// makeMember manufactures a type token for the package and the given module and type.
func makeMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
}

// makeType manufactures a type token for the package and the given module and type.
func makeType(mod string, typ string) tokens.Type {
	return tokens.Type(makeMember(mod, typ))
}

// makeDataSource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the data source's
// first character.
func makeDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeMember(mod+"/"+fn, res)
}

// makeResource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the resource's
// first character.
func makeResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeType(mod+"/"+fn, res)
}

// boolRef returns a reference to the bool argument.
func boolRef(b bool) *bool {
	return &b
}

// stringValue gets a string value from a property map if present, else ""
func stringValue(vars resource.PropertyMap, prop resource.PropertyKey) string {
	val, ok := vars[prop]
	if ok && val.IsString() {
		return val.StringValue()
	}
	return ""
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c *terraform.ResourceConfig) error {
	return nil
}

// managedByPulumi is a default used for some managed resources, in the absence of something more meaningful.
var managedByPulumi = &tfbridge.DefaultInfo{Value: "Managed by Pulumi"}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := spotinst.Provider().(*schema.Provider)

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "spotinst",
		Description: "A Pulumi package for creating and managing spotinst cloud resources.",
		Keywords:    []string{"pulumi", "spotinst"},
		License:     "Apache-2.0",
		Homepage:    "https://pulumi.io",
		Repository:  "https://github.com/timmyers/pulumi-spotinst",
		Config: map[string]*tfbridge.SchemaInfo{
			"account": {
				Default: &tfbridge.DefaultInfo{
					Value:   "",
					EnvVars: []string{"SPOTINST_ACCOUNT"},
				},
			},
			"token": {
				Default: &tfbridge.DefaultInfo{
					Value:   "",
					EnvVars: []string{"SPOTINST_TOKEN"},
				},
			},
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"spotinst_elastigroup_aws":           {Tok: makeResource(awsMod, "Elastigroup")},
			"spotinst_elastigroup_aws_beanstalk": {Tok: makeResource(awsMod, "Beanstalk")},
			"spotinst_elastigroup_azure":         {Tok: makeResource(azureMod, "Elastigroup")},
			"spotinst_elastigroup_gcp": {
				Tok: makeResource(gcpMod, "Elastigroup"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"gpu": {Name: "gpu"},
				},
			},
			"spotinst_elastigroup_gke": {
				Tok: makeResource(gkeMod, "Elastigroup"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"gpu": {Name: "gpu"},
				},
			},
			"spotinst_mrscaler_aws":                 {Tok: makeResource(awsMod, "MrScalar")},
			"spotinst_multai_balancer":              {Tok: makeResource(multaiMod, "Balancer")},
			"spotinst_multai_deployment":            {Tok: makeResource(multaiMod, "Deployment")},
			"spotinst_multai_listener":              {Tok: makeResource(multaiMod, "Listener")},
			"spotinst_multai_routing_rule":          {Tok: makeResource(multaiMod, "RoutingRule")},
			"spotinst_multai_target":                {Tok: makeResource(multaiMod, "Target")},
			"spotinst_multai_target_set":            {Tok: makeResource(multaiMod, "TargetSet")},
			"spotinst_ocean_aws":                    {Tok: makeResource(awsMod, "Ocean")},
			"spotinst_ocean_aws_launch_spec":        {Tok: makeResource(awsMod, "OceanLaunchSpec")},
			"spotinst_ocean_ecs":                    {Tok: makeResource(ecsMod, "Ocean")},
			"spotinst_ocean_ecs_launch_spec":        {Tok: makeResource(ecsMod, "OceanLaunchSpec")},
			"spotinst_ocean_gke_import":             {Tok: makeResource(gkeMod, "OceanImport")},
			"spotinst_ocean_gke_launch_spec":        {Tok: makeResource(gkeMod, "OceanLaunchSpec")},
			"spotinst_ocean_gke_launch_spec_import": {Tok: makeResource(gkeMod, "OceanLaunchSpecImport")},
			"spotinst_subscription":                 {Tok: makeResource(subscriptionMod, "Subscription")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: makeDataSource(mainMod, "getAmi")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "latest",
			},
			DevDependencies: map[string]string{
				"@types/node": "^8.0.25", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=1.0.0,<2.0.0",
			},
		},
	}

	// For all resources with name properties, we will add an auto-name property.  Make sure to skip those that
	// already have a name mapping entry, since those may have custom overrides set above (e.g., for length).
	const nameProperty = "name"
	for resname, res := range prov.Resources {
		if schema := p.ResourcesMap[resname]; schema != nil {
			// Only apply auto-name to input properties (Optional || Required) named `name`
			if tfs, has := schema.Schema[nameProperty]; has && (tfs.Optional || tfs.Required) {
				if _, hasfield := res.Fields[nameProperty]; !hasfield {
					if res.Fields == nil {
						res.Fields = make(map[string]*tfbridge.SchemaInfo)
					}
					res.Fields[nameProperty] = tfbridge.AutoName(nameProperty, 255)
				}
			}
		}
	}

	return prov
}
