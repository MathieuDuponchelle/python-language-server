# Copyright 2017 Palantir Technologies, Inc.
import logging
from .base import JediProvider
from pyls.vscode import SymbolKind

log = logging.getLogger(__name__)


class JediDocumentSymbolsProvider(JediProvider):
    """ Finds all symbols in a given text document """

    def run(self, doc_uri):
        definitions = self.jedi_names(doc_uri)
        log.info(definitions)

        return [{
            'name': d.name,
            'kind': _kind(d),
            'location': {'uri': doc_uri, 'range': _range(d)}
        } for d in definitions]


def _range(d):
    return {
        'start': {'line': d.line - 1, 'character': d.column},
        'end': {'line': d.line - 1, 'character': d.column + len(d.name)}
    }


def _kind(d):
    """ Return the VSCode Symbol Type """
    MAP = {
        'none': SymbolKind.Variable,
        'type': SymbolKind.Class,
        'tuple': SymbolKind.Class,
        'dict': SymbolKind.Class,
        'dictionary': SymbolKind.Class,
        'function': SymbolKind.Function,
        'lambda': SymbolKind.Function,
        'generator': SymbolKind.Function,
        'class': SymbolKind.Class,
        'instance': SymbolKind.Class,
        'method': SymbolKind.Method,
        'builtin': SymbolKind.Class,
        'builtinfunction': SymbolKind.Function,
        'module': SymbolKind.Module,
        'file': SymbolKind.File,
        'xrange': SymbolKind.Array,
        'slice': SymbolKind.Class,
        'traceback': SymbolKind.Class,
        'frame': SymbolKind.Class,
        'buffer': SymbolKind.Array,
        'dictproxy': SymbolKind.Class,
        'funcdef': SymbolKind.Function,
        'property': SymbolKind.Property,
        'import': SymbolKind.Module,
        'keyword': SymbolKind.Variable,
        'constant': SymbolKind.Constant,
        'variable': SymbolKind.Variable,
        'value': SymbolKind.Variable,
        'param': SymbolKind.Variable,
        'statement': SymbolKind.Variable,
        'boolean': SymbolKind.Boolean,
        'int': SymbolKind.Number,
        'longlean': SymbolKind.Number,
        'float': SymbolKind.Number,
        'complex': SymbolKind.Number,
        'string': SymbolKind.String,
        'unicode': SymbolKind.String,
        'list': SymbolKind.Array,
    }

    return MAP.get(d.type)
