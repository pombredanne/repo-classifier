from github import Repository
from github.GitTree import GitTree
from github.GithubException import GithubException

from classification.Feature import Feature
from classification.feature_extraction.FeatureExtractor import FeatureExtractor


class BranchExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Number of branches')]

    def extract_features(self) -> [Feature]:
        branches = self.repo.get_branches()
        num = len([branch for branch in branches])
        self.features[0].value = num
        return self.features


class CommitNumberExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Number of commits')]

    def extract_features(self) -> [Feature]:
        contributors = self.repo.get_contributors()
        total_commits_default_branch = sum(contributor.contributions for contributor in contributors)
        self.features[0].value = total_commits_default_branch
        return self.features


class ContributorsExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Number of contributors')]

    def extract_features(self) -> [Feature]:
        contributors = self.repo.get_contributors()
        num = len([c for c in contributors])
        self.features[0].value = num
        return self.features


class ForkExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Number of forks')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = self.repo.forks
        return self.features


class HasBuildFileExtractor(FeatureExtractor):
    # TODO: Add more build files
    build_files = ['build.gradle', 'composer.json', 'makefile' 'package.json', 'pom.xml']

    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Has build file')]

    def extract_features(self) -> [Feature]:
        try:
            files = self.repo.get_dir_contents('')
        except GithubException:
            files = []

        self.features[0].value = 0
        for file in files:
            if file.name and file.name.lower() in self.build_files:
                self.features[0].value = 1
        return self.features


class HasDownloadsExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Has downloads')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = 1 if self.repo.has_downloads else 0
        return self.features


class HasIssuesExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Has issues')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = 1 if self.repo.has_issues else 0
        return self.features


class HasWikiExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Has wiki')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = 1 if self.repo.has_wiki else 0
        return self.features


class IsForkExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Is a fork')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = 1 if self.repo.fork else 0
        return self.features


class DescriptionKeyWordExtractor(FeatureExtractor):
    # TODO: Add more keywords
    keywords = ['homework', 'lecture', 'course', 'framework']

    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Contains keyword "' + keyword + '"') for keyword in self.keywords]

    def extract_features(self):
        description = self.repo.description.lower() if self.repo.description else ''

        for keyword, feature in zip(self.keywords, self.features):
            if keyword in description:
                feature.value = 1
            else:
                feature.value = 0
        return self.features


class OpenIssueExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Number of open issues')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = self.repo.open_issues_count
        return self.features


class SizeExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Size of repo')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = self.repo.size
        return self.features


class StarExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Number of stars')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = self.repo.stargazers_count
        return self.features


class TotalFilesExtractor(FeatureExtractor):
    """
    Extractor for returning the total number of files for the default branch of the repository.
    """

    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Number of files')]

    def extract_features(self) -> [Feature]:
        # Not sure if master is always the best approach. Maybe it is better to request the latest commit and use the
        # SHA of it
        # Boolean flag -> recursive call for contents
        total_num_files = self._get_num_files(self.repo.get_git_tree('master', True))
        self.features[0].value = total_num_files
        return self.features

    def _get_num_files(self, tree: GitTree) -> int:
        num_files = 0
        for item in tree.tree:
            if item.type == 'blob':
                num_files += 1
                # Because of recursive call ignore dirs seems to be working also with folders with 10000 files
        return num_files


class WatchersExtractor(FeatureExtractor):
    def __init__(self, repo: Repository):
        super().__init__(repo)
        self.features = [Feature('Number of watchers')]

    def extract_features(self) -> [Feature]:
        self.features[0].value = self.repo.watchers_count
        return self.features
