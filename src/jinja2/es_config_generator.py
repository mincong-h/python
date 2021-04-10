import os
from typing import NamedTuple

from jinja2 import FileSystemLoader, Environment


class ElasticsearchConfig(NamedTuple):
    cluster_name: str
    node_name: str


def render_config(cluster_name: str, node_id: int) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("elasticsearch.yml.j2")
    es = ElasticsearchConfig(
        cluster_name=cluster_name, node_name=f"{cluster_name}-data-{node_id}"
    )
    return template.render(es=es)
