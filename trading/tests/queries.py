from django.test.testcases import TestCase
import graphene
from graphene_django.types import DjangoObjectType
from trading.models import Instruments


class TestResolves(TestCase):

    def test_should_query_well(self):
        class InstrumentType(DjangoObjectType):
            class Meta:
                model = Instruments
                fields = "__all__"

        class Query(graphene.ObjectType):
            instrument = graphene.Field(InstrumentType)

            def resolve_instrument(root, info):
                return Instruments(id="100", name="BLUEPRINT MEDICINES CORP", symbol="BPMC")

        query = """
            query InstrumentQuery {
            instrument {
                id,
                name,
                symbol
            }
            }
        """
        expected = {"instrument": {"id": "100", "name": "BLUEPRINT MEDICINES CORP", "symbol": "BPMC"}}
        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        print(result)
        assert not result.errors
        assert result.data == expected