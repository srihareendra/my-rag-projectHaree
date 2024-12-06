from azure_config import AzureConfig
import os, uuid
# set environment variables before importing any other code
from dotenv import load_dotenv
load_dotenv()

from azure.ai.ml import MLClient
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment, Model, Environment, BuildContext
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.models import RoleAssignmentCreateParameters
from azure.core.exceptions import ResourceExistsError
# Read configuration
azure_config = AzureConfig()

from azure.ai.ml import MLClient
print("Initializing MLClient...")
client = MLClient(
    DefaultAzureCredential(),
    azure_config.subscription_id,
    azure_config.resource_group,
    azure_config.workspace_name
)