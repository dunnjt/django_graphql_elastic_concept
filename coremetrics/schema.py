import graphene
from graphene_django import DjangoObjectType

from .models import CoreMetrics


class CoreMetricsType(DjangoObjectType):
    class Meta:
        model = CoreMetrics


class Query(graphene.ObjectType):
    coremetrics = graphene.List(CoreMetricsType)

    def resolve_coremetrics(self, info, **kwargs):
        return CoreMetrics.objects.all()


class CreateCoreMetrics(graphene.Mutation):
    id = graphene.Int()
    data = graphene.String()

    #2
    class Arguments:
        data = graphene.String()

    #3
    def mutate(self, info, data):
        coremetrics = CoreMetrics(data=data)
        coremetrics.save()

        return CreateCoreMetrics(
            id=coremetrics.id,
            data=coremetrics.data,
        )


#4
class Mutation(graphene.ObjectType):
    create_coremetrics = CreateCoreMetrics.Field()