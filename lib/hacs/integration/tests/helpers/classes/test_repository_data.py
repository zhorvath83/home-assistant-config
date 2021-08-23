from custom_components.hacs.helpers.classes.repositorydata import RepositoryData


def test_guarded():
    data = RepositoryData.create_from_dict({"full_name": "test"})
    assert data.name == "test"

    data.update_data({"name": "new"})
    assert data.name != "new"

    test = data.to_json()
    test["name"] = "new"

    assert data.name != "new"

    export = data.export_data()
    assert isinstance(export, dict)
    data.memorize_storage(export)
    assert data.export_data() is None
