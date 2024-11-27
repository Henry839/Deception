"""World Builder

Build the full set W, which contains all the propositions involved
"""
from allennlp.predictors.predictor import Predictor

class WorldBuilder():
    """World Builder

    Build the full set W, which contains all the propositions involved.
    Approaches: 1) Knowledge Graph (Each proposition is a triplet)

    Attributes:
        build_type: type of approach to build W
        model: model used to generate W
        W_set: full set W, a list
    """
    def __init__(self, 
                 build_type: str = "KG",):
        """Initialization.

        Args:
            build_type: type of approach to build W
                        "KG": Knowledge Graph
        Raises:
            ValueError: invalid build type

        """
        self.build_type = build_type

        if build_type == "KG":
            # use pre-trained OpenIE model
            self.model = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/openie-model.2020.03.26.tar.gz")
        else:
            raise ValueError(f"{build_type} is invalid for build_type")

        self.W_set = []

    from .build import KG_Build


