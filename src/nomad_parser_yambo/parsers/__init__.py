from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class YAMBOParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_parser_yambo.parsers.parser import YAMBOParser

        return YAMBOParser(**self.dict())


nomad_parser_yambo_plugin = YAMBOParserEntryPoint(
    name='YAMBOParser',
    description='Entry point for the YAMBO parser.',
    mainfile_contents_re=r'Build.+\s+http://www\.yambo-code\.org',
)
