"""
Class object for AIOGitHubAPIOrgsTeam
Documentation: https://docs.github.com/en/rest/reference/teams#get-a-team-by-name

Generated by generate/generate.py - 2020-08-02 10:33:09.248066
"""
from aiogithubapi.objects.base import AIOGitHubAPIBase


class Organization(AIOGitHubAPIBase):
    @property
    def login(self):
        return self.attributes.get("login", "")

    @property
    def id(self):
        return self.attributes.get("id", None)

    @property
    def node_id(self):
        return self.attributes.get("node_id", "")

    @property
    def url(self):
        return self.attributes.get("url", "")

    @property
    def repos_url(self):
        return self.attributes.get("repos_url", "")

    @property
    def events_url(self):
        return self.attributes.get("events_url", "")

    @property
    def hooks_url(self):
        return self.attributes.get("hooks_url", "")

    @property
    def issues_url(self):
        return self.attributes.get("issues_url", "")

    @property
    def members_url(self):
        return self.attributes.get("members_url", "")

    @property
    def public_members_url(self):
        return self.attributes.get("public_members_url", "")

    @property
    def avatar_url(self):
        return self.attributes.get("avatar_url", "")

    @property
    def description(self):
        return self.attributes.get("description", "")

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def company(self):
        return self.attributes.get("company", "")

    @property
    def blog(self):
        return self.attributes.get("blog", "")

    @property
    def location(self):
        return self.attributes.get("location", "")

    @property
    def email(self):
        return self.attributes.get("email", "")

    @property
    def twitter_username(self):
        return self.attributes.get("twitter_username", "")

    @property
    def is_verified(self):
        return self.attributes.get("is_verified", True)

    @property
    def has_organization_projects(self):
        return self.attributes.get("has_organization_projects", True)

    @property
    def has_repository_projects(self):
        return self.attributes.get("has_repository_projects", True)

    @property
    def public_repos(self):
        return self.attributes.get("public_repos", None)

    @property
    def public_gists(self):
        return self.attributes.get("public_gists", None)

    @property
    def followers(self):
        return self.attributes.get("followers", None)

    @property
    def following(self):
        return self.attributes.get("following", None)

    @property
    def html_url(self):
        return self.attributes.get("html_url", "")

    @property
    def created_at(self):
        return self.attributes.get("created_at", "")

    @property
    def type(self):
        return self.attributes.get("type", "")


class AIOGitHubAPIOrgsTeam(AIOGitHubAPIBase):
    @property
    def id(self):
        return self.attributes.get("id", None)

    @property
    def node_id(self):
        return self.attributes.get("node_id", "")

    @property
    def url(self):
        return self.attributes.get("url", "")

    @property
    def html_url(self):
        return self.attributes.get("html_url", "")

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def slug(self):
        return self.attributes.get("slug", "")

    @property
    def description(self):
        return self.attributes.get("description", "")

    @property
    def privacy(self):
        return self.attributes.get("privacy", "")

    @property
    def permission(self):
        return self.attributes.get("permission", "")

    @property
    def members_url(self):
        return self.attributes.get("members_url", "")

    @property
    def repositories_url(self):
        return self.attributes.get("repositories_url", "")

    @property
    def parent(self):
        return self.attributes.get("parent", None)

    @property
    def members_count(self):
        return self.attributes.get("members_count", None)

    @property
    def repos_count(self):
        return self.attributes.get("repos_count", None)

    @property
    def created_at(self):
        return self.attributes.get("created_at", "")

    @property
    def updated_at(self):
        return self.attributes.get("updated_at", "")

    @property
    def organization(self):
        return Organization(self.attributes.get("organization", {}))
