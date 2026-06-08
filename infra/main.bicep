targetScope = 'subscription'

param resourceGroupName string = 'rg-tenderpilot-ai'
param location string = 'eastus'
param openAiModelName string = 'gpt-4o'
param openAiModelVersion string = '2024-05-13'

resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: resourceGroupName
  location: location
}

module resources 'resources.bicep' = {
  name: 'tenderpilot-azure-deploy'
  scope: rg
  params: {
    location: location
    openAiModelName: openAiModelName
    openAiModelVersion: openAiModelVersion
  }
}

// Inline nested resources definition to keep deployment atomic and transparent
// File: infra/resources.bicep
/*
param location string
param openAiModelName string
param openAiModelVersion string

// 1. User Assigned Managed Identity
resource managedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-tenderpilot-workforce'
  location: location
}

// 2. Azure Key Vault
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: 'kv-tenderpilot-${uniqueString(resourceGroup().id)}'
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
  }
}

// 3. Azure Cosmos DB Account (NoSQL & Gremlin Graph capability)
resource cosmosAccount 'Microsoft.DocumentDB/databaseAccounts@2023-11-15' = {
  name: 'cosmos-tenderpilot-${uniqueString(resourceGroup().id)}'
  location: location
  properties: {
    databaseAccountOfferType: 'Standard'
    locations: [
      {
        locationName: location
        failoverPriority: 0
        isZoneRedundant: false
      }
    ]
    capabilities: [
      { name: 'EnableGremlin' }
    ]
  }
}

// 4. Azure OpenAI Account
resource openAiAccount 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: 'cog-tenderpilot-openai-${uniqueString(resourceGroup().id)}'
  location: location
  kind: 'OpenAI'
  sku: {
    name: 'S0'
  }
  properties: {
    customSubDomainName: 'tenderpilot-ai-portal-${uniqueString(resourceGroup().id)}'
  }
}

resource openAiDeployment 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  parent: openAiAccount
  name: 'gpt-4o-deployment'
  properties: {
    model: {
      format: 'OpenAI'
      name: openAiModelName
      version: openAiModelVersion
    }
  }
  sku: {
    name: 'Standard'
    capacity: 20
  }
}

// 5. Azure AI Search Service (Past Proposals RAG index)
resource searchService 'Microsoft.Search/searchServices@2023-11-01' = {
  name: 'srch-tenderpilot-kb-${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'basic'
  }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
  }
}

// 6. Azure Storage Account (Specifications PDFs blobs)
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'sttenderpilotalerts${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

// 7. Azure AI Foundry Hub (Azure AI Workspace)
resource aiHub 'Microsoft.MachineLearningServices/workspaces@2023-10-01' = {
  name: 'ai-hub-tenderpilot'
  location: location
  kind: 'hub'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    description: 'TenderPilot AI Operations Workspace Hub'
    keyVault: keyVault.id
    storageAccount: storageAccount.id
  }
}

// 8. Azure Service Bus (Agent Orchestration Event Bus)
resource serviceBusNamespace 'Microsoft.ServiceBus/namespaces@2022-10-01-preview' = {
  name: 'sb-tenderpilot-bus-${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'Standard'
  }
}

// 9. Azure Container Apps Env
resource containerAppEnv 'Microsoft.App/managedEnvironments@2024-03-01' = {
  name: 'cae-tenderpilot-workforce'
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalytics.properties.customerId
        sharedKey: logAnalytics.listKeys().primarySharedKey
      }
    }
  }
}

// 10. Log Analytics & App Insights
resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2021-06-01' = {
  name: 'log-tenderpilot-monitor'
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'appinsights-tenderpilot'
  location: location
  kind: 'web'
  properties: {
    WorkspaceResourceId: logAnalytics.id
  }
}
*/
