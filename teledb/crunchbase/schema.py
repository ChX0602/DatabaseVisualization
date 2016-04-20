from graphene import relay, ObjectType
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode
from crunchbase.models import *


class FundingRoundNode(DjangoNode):
	class Meta:
		model = CbFundingRounds


class ObjectNode(DjangoNode):
	class Meta:
		model = CbObjects


class RelationshipNode(DjangoNode):
	class Meta:
		model = CbRelationships


class DegreeNode(DjangoNode):
	class Meta:
		model = CbDegrees


class AcquisitionNode(DjangoNode):
	class Meta:
		model = CbAcquisitions


class FundNode(DjangoNode):
	class Meta:
		model = CbFunds


class InvestmentNode(DjangoNode):
	class Meta:
		model = CbInvestments


class IpoNode(DjangoNode):
	class Meta:
		model = CbIpos


class MilestoneNode(DjangoNode):
	class Meta:
		model = CbMilestones


class OfficeNode(DjangoNode):
	class Meta:
		model = CbOffices


class PeopleNode(DjangoNode):
	class Meta:
		model = CbPeople


class Query(ObjectType):
	fundingRound = relay.NodeField(FundingRoundNode)
	allFundingRounds = DjangoFilterConnectionField(FundingRoundNode)

	object = relay.NodeField(ObjectNode)
	allObjects = DjangoFilterConnectionField(ObjectNode)

	relationship = relay.NodeField(RelationshipNode)
	allRelationships = DjangoFilterConnectionField(RelationshipNode)

	degree = relay.NodeField(DegreeNode)
	allDegrees = DjangoFilterConnectionField(DegreeNode)

	acquisition = relay.NodeField(AcquisitionNode)
	allAcquisitions = DjangoFilterConnectionField(AcquisitionNode)

	fund = relay.NodeField(FundNode)
	allFunds = DjangoFilterConnectionField(FundNode)

	investment = relay.NodeField(InvestmentNode)
	allInvestments = DjangoFilterConnectionField(InvestmentNode)

	ipo = relay.NodeField(IpoNode)
	allIpos = DjangoFilterConnectionField(IpoNode)

	milestone = relay.NodeField(MilestoneNode)
	allMilestones = DjangoFilterConnectionField(MilestoneNode)

	office = relay.NodeField(OfficeNode)
	allOffices = DjangoFilterConnectionField(OfficeNode)

	people = relay.NodeField(PeopleNode)
	allPeople = DjangoFilterConnectionField(PeopleNode)

	class Meta:
		abstract = True