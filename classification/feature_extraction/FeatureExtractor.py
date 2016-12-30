import abc

from github.Repository import Repository

from classification.models import Feature


class FeatureExtractor:
    """
    Base class for all feature extractors.
    """

    def __init__(self, repo: Repository):
        self.repo = repo
        self.features = []

    @abc.abstractmethod
    def extract_features(self) -> [Feature]:
        """
        :return: Feature
        """
        raise NotImplementedError('Main class should not be called for feature extraction!')
