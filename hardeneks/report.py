from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich import print

from tabulate import tabulate

console = Console()


def export_data(headers, values, message, docs, type=None):
    with open('harden_report.txt', 'a') as f:
        f.write("{0:-^40}".format(f" {message.replace('[red]', '')} "))
        f.write('\n')
        if type:
            f.write("{0:^40}".format(f" {type} "))
            f.write('\n')
        f.write(tabulate(values, headers=headers))
        f.write('\n')
        f.write("{0:^40}".format(f" {docs.replace('[link=', '').replace(']Click to see the guide[/link]', '')} "))
        f.write('\n\n\n')


def print_role_table(roles, message, docs, type):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    headers = ["Kind", "Namespace", "Name"]
    values = []

    for role in roles:
        table.add_row(type, role.metadata.namespace, role.metadata.name)
        values.append([role.metadata.namespace, role.metadata.name])

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs, type)


def print_instance_metadata_table(instances, message, docs):
    table = Table()

    table.add_column("InstanceId", style="cyan")
    table.add_column("HttpPutResponseHopLimit", style="magenta")

    headers = ["InstanceId", "HttpPutResponseHopLimit"]
    values = []

    for instance in instances:
        table.add_row(
            instance["Instances"][0]["InstanceId"],
            str(
                instance["Instances"][0]["MetadataOptions"][
                    "HttpPutResponseHopLimit"
                ]
            ),
        )
        values.append(
            [
                instance["Instances"][0]["InstanceId"],
                str(
                    instance["Instances"][0]["MetadataOptions"][
                        "HttpPutResponseHopLimit"
                    ]
                )
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)


def print_instance_public_table(instances, message, docs):
    table = Table()

    table.add_column("InstanceId", style="cyan")
    table.add_column("PublicDnsName", style="magenta")

    headers = ["InstanceId", "PublicDnsName"]
    values = []

    for instance in instances:
        table.add_row(
            instance["Instances"][0]["InstanceId"],
            str(instance["Instances"][0]["PublicDnsName"]),
        )
        values.append(
            [
                instance["Instances"][0]["InstanceId"],
                str(instance["Instances"][0]["PublicDnsName"])
            ]
        )

    print(Panel(table, title=message))
    console.print()
    export_data(headers, values, message, docs)


def print_repository_table(repositories, attribute, message, docs):
    table = Table()
    table.add_column("Repository", style="cyan")
    table.add_column(attribute, style="magenta")

    headers = ["Repository", attribute]
    values = []

    for repository in repositories:
        table.add_row(
            repository["repositoryName"],
            repository[attribute],
        )
        values.append(
            [
                repository["repositoryName"],
                repository[attribute]
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)


def print_pod_table(pods, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    headers = ["Kind", "Namespace", "Name"]
    values = []

    for pod in pods:
        table.add_row("Pod", pod.metadata.namespace, pod.metadata.name)
        values.append(
            [
                "Pod", pod.metadata.namespace, pod.metadata.name
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)


def print_workload_table(workloads, message, docs, kind):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    headers = ["Kind", "Namespace", "Name"]
    values = []

    for workload in workloads:
        table.add_row(
            kind, workload.metadata.namespace, workload.metadata.name
        )
        values.append(
            [
                kind, workload.metadata.namespace, workload.metadata.name
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)


def print_namespace_table(namespaces, message, docs):
    table = Table()

    table.add_column("Namespace", style="cyan")

    headers = ["Namespace"]
    values = []

    for namespace in namespaces:
        table.add_row(
            namespace,
        )
        values.append(
            [
                namespace
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)


def print_service_table(services, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    headers = ["Kind", "Namespace", "Name"]
    values = []

    for workload in services:
        table.add_row(
            "Service", workload.metadata.namespace, workload.metadata.name
        )
        values.append(
            [
                "Service", workload.metadata.namespace, workload.metadata.name
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)


def print_deployment_table(deployments, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    headers = ["Kind", "Namespace", "Name"]
    values = []

    for workload in deployments:
        table.add_row(
            "Deployment", workload.metadata.namespace, workload.metadata.name
        )
        values.append(
            [
                "Deployment", workload.metadata.namespace, workload.metadata.name
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)


def print_storage_class_table(storage_classes, message, docs):
    table = Table()

    table.add_column("StorageClass", style="cyan")
    table.add_column("Encyrpted", style="magenta")

    headers = ["StorageClass", "Encyrpted"]
    values = []

    for storage_class in storage_classes:
        table.add_row(storage_class.metadata.name, "false")
        values.append(
            [
                storage_class.metadata.name, "false"
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)


def print_persistent_volume_table(persistent_volumes, message, docs):
    table = Table()

    table.add_column("PersistentVolume", style="cyan")
    table.add_column("Encrypted", style="magenta")

    headers = ["PersistentVolume", "Encyrpted"]
    values = []

    for persistent_volume in persistent_volumes:
        table.add_row(persistent_volume.metadata.name, "false")
        values.append(
            [
                persistent_volume.metadata.name, "false"
            ]
        )

    print(Panel(table, title=message, subtitle=docs))
    console.print()
    export_data(headers, values, message, docs)
