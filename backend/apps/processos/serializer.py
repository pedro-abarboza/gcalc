from rest_framework import serializers
from ..processos.models import *


class ReclamadasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reclamadas
        fields = ['nome']
    

class ReclamantesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reclamantes
        fields = ['nome']
    
    
class ProcessosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Processos
        fields = ['n_processo','reclamada','reclamante',
                  'dt_ajuizamento','formato','dt_ult_atualizacao',
                  'dt_ult_verificacao']


class AndamentosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Andamentos
        fields = ['processo','descricao','codigo','grau','dt_andamento']
