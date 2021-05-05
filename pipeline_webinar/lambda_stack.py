from aws_cdk import core as cdk
from os import path
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
import aws_cdk.aws_lambda as lmd
from aws_cdk import aws_iam as iam
import aws_cdk.aws_apigateway as apigw

env='l2'
class LambdaStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        role_arn = 'arn:aws:iam::315207712355:role/lbrole'
        role=iam.Role.from_role_arn(self, id='role_id', role_arn=role_arn)
        this_dir = path.dirname(__file__)
        handler = lmd.Function(self, 'Handler',
                               function_name=construct_id+"HandlerFunction",
                               role=role,
                               runtime=lmd.Runtime.PYTHON_3_7,
                               handler='handler.handler',
                               code=lmd.Code.from_asset(path.join(this_dir, 'lambda'))

                               )