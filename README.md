# 🚀 Scaling EKS Cluster with Custom Events

This project demonstrates how to automatically scale an Amazon EKS cluster based on custom events using AWS Lambda and EventBridge. By monitoring custom metrics and adjusting the desired node count of the EKS cluster, this solution enables seamless scaling to handle varying workload demands.

## Usage

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd scaling-eks-cluster
   ```

3. Deploy the Lambda function using AWS SAM CLI:
   ```bash
   sam deploy --guided
   ```

4. Follow the instructions provided by AWS SAM CLI to configure the deployment.

5. Once the deployment is complete, the Lambda function will be triggered automatically based on EKS cluster events.

## Benefits

- **Automatic Scaling**: The Lambda function monitors custom metrics and dynamically adjusts the desired node count of the EKS cluster based on workload demands, ensuring optimal resource allocation.

- **Cost Optimization**: By scaling the cluster up or down as needed, this solution helps optimize costs by aligning resource usage with actual workload requirements.

- **Efficient Resource Management**: With automatic scaling, you can ensure that your EKS cluster is always right-sized, providing the necessary resources to handle varying workloads effectively.

- **Simplified Operations**: This solution automates the scaling process, reducing the need for manual intervention and simplifying cluster management.

- **Flexible Customization**: The project can be customized to monitor specific custom metrics and implement scaling strategies tailored to your application's requirements.

---

Feel free to explore the code and customize it according to your specific needs. If you encounter any issues or have suggestions for improvements, please don't hesitate to open an issue or submit a pull request.

Let's scale your EKS clusters effortlessly! 🚀
```

Feel free to modify the content or add more sections to suit your project's specific requirements.
