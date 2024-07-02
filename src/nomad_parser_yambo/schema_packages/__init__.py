from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class YAMBOSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_parser_yambo.schema_packages.package import m_package

        return m_package


nomad_parser_yambo_schema = YAMBOSchemaPackageEntryPoint(
    name='YAMBOSchemaPackage',
    description='Entry point for the YAMBO code-specific schema.',
)
