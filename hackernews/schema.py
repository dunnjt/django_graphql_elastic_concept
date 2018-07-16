import graphene

import coremetrics.schema


class Query(coremetrics.schema.Query, graphene.ObjectType):
    pass

class Mutation(coremetrics.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)