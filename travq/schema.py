import graphene
from graphene_django import DjangoObjectType

from .models import Questions, Answers, User, Tags


class QuestionType(DjangoObjectType):
    class Meta:
        model = Questions


class UserType(DjangoObjectType):
    class Meta:
        model = User

class AnswersType(DjangoObjectType):
    class Meta:
        model = Answers

class TagsType(DjangoObjectType):
    class Meta:
        model = Tags

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionsType)
    user = graphene.List(UserType)
    answers = graphene.List(AnswersType)
    tags = graphene.List(TagsType)

    def resolve_questions(self, info, **kwargs):
        return Questions.objects.all()
    
    def resolve_user(self, info, **kwargs):
        return User.objects.all()
        
    def resolve_Answers(self, info, **kwargs):
        return Answers.objects.all()
    
    def resolve_Tags(self, info, **kwargs):
        return Tags.objects.all()


class CreateTags(graphene.Mutation):
    id = graphene.Int()
    tags = graphene.String()

    #2
    class Arguments:
        tags = graphene.String()

    #3
    def mutate(self, info, data):
        tags = Tags(tag=tag)
        tags.save()

        return CreateTags(
            id=tags.id,
            tag=tags.tag,
        )

class Mutation(graphene.ObjectType):
    create_tags = CreateTags.Field()