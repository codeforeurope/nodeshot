# this app is dependant on "nodes"
from django.conf import settings
if 'nodeshot.core.nodes' not in settings.INSTALLED_APPS:
    from nodeshot.core.base.exceptions import DependencyError
    raise DependencyError('nodeshot.community.participation depends on nodeshot.core.nodes, which should be in settings.INSTALLED_APPS')


from comment import Comment
from vote import Vote
from rating import Rating

from node_participation_settings import NodeParticipationSettings
from node_rating_count import NodeRatingCount
from django.core.exceptions import ObjectDoesNotExist

__all__ = [
    'NodeRatingCount',
    'Comment',
    'Vote',
    'Rating',
    'NodeParticipationSettings',
]


### ------ Layers Operations ------ ###


if 'nodeshot.core.layers' in settings.INSTALLED_APPS:
    from layer_participation_settings import LayerParticipationSettings
    
    __all__ += ['LayerParticipationSettings']
    
    from nodeshot.core.layers.models import Layer
    
    @property
    def _layer_participation_settings(self):
        """
        Return layer_participation_settings record
        or create it if it does not exist
        
        usage:
        layer = Layer.objects.get(pk=1)
        layer.participation_settings
        """
        try:
            return self.layer_participation_settings
        except ObjectDoesNotExist:
            layer_participation_settings = LayerParticipationSettings(layer=self)
            layer_participation_settings.save()
            return layer_participation_settings
    
    Layer.participation_settings = _layer_participation_settings


### ------ Add methods to Node Model ------ ###


from nodeshot.core.nodes.models import Node

@property
def _node_rating_count(self):
    """
    Return node_rating_count record
    or create it if it does not exist
    
    usage:
    node = Node.objects.get(pk=1)
    node.rating_count
    """
    try:
        return self.noderatingcount
    except ObjectDoesNotExist:
        node_rating_count = NodeRatingCount(node=self)
        node_rating_count.save()
        return node_rating_count

Node.rating_count = _node_rating_count

@property
def _node_participation_settings(self):
    """
    Return node_participation_settings record
    or create it if it does not exist
    
    usage:
    node = Node.objects.get(pk=1)
    node.participation_settings
    """
    try:
        return self.node_participation_settings
    except ObjectDoesNotExist:
        node_participation_settings = NodeParticipationSettings(node=self)
        node_participation_settings.save()
        return node_participation_settings

Node.participation_settings = _node_participation_settings


### SIGNALS ###


from django.dispatch import receiver
from django.db.models.signals import post_save
from nodeshot.core.nodes.models import Node

@receiver(post_save, sender=Node)
def create_node_rating_counts(sender, **kwargs):
    """ create node rating count """
    created = kwargs['created']
    node = kwargs['instance']
    if created:
        # create node_rating_count 
        node_rating_count = NodeRatingCount(node=node)
        node_rating_count.save()