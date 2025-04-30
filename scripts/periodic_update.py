from fetch_sf_hw import fetch_and_cache_repos
from gen_hw_doc import gen_hw_doc
from fetch_changelog import fetch_changelog_and_save


def main():
    fetch_and_cache_repos()
    gen_hw_doc()
    fetch_changelog_and_save()


if __name__ == "__main__":
    main()
