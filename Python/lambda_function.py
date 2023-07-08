import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Specify your EKS cluster name
    cluster_name = 'your-eks-cluster'

    # Specify the custom metric threshold for scaling
    metric_threshold = 500

    # Specify the scaling adjustment
    scaling_adjustment = 1

    # Specify the minimum and maximum node counts
    min_node_count = 1
    max_node_count = 10

    # Create an EKS client
    eks_client = boto3.client('eks')

    # Get the current EKS cluster configuration
    response = eks_client.describe_cluster(name=cluster_name)
    current_node_count = response['cluster']['scalingConfig']['desiredSize']

    # Get the custom metric value
    cloudwatch_client = boto3.client('cloudwatch')
    metric_data = cloudwatch_client.get_metric_statistics(
        Namespace='YourMetricNamespace',
        MetricName='YourCustomMetric',
        Dimensions=[
            {
                'Name': 'ClusterName',
                'Value': cluster_name
            },
        ],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Average']
    )

    if len(metric_data['Datapoints']) > 0:
        average_value = metric_data['Datapoints'][0]['Average']

        # Scale up or down based on the custom metric value
        if average_value > metric_threshold:
            new_node_count = min(current_node_count + scaling_adjustment, max_node_count)
        else:
            new_node_count = max(current_node_count - scaling_adjustment, min_node_count)

        # Update the EKS cluster desired node count
        eks_client.update_nodegroup_config(
            clusterName=cluster_name,
            nodegroupName='your-node-group',
            scalingConfig={
                'minSize': min_node_count,
                'maxSize': max_node_count,
                'desiredSize': new_node_count
            }
        )
