import pytest

from lucid.modelzoo.aligned_activations import NUMBER_OF_AVAILABLE_SAMPLES
from lucid.modelzoo.vision_models import AlexNet, InceptionV1
from lucid.recipes.activation_atlas import activation_atlas, aligned_activation_atlas
from lucid.misc.io import save

# TODO(schubert@): think of actually automatable tests?

# Run test with just 1/10th of available samples
subset = NUMBER_OF_AVAILABLE_SAMPLES // 10


@pytest.mark.slow
def test_activation_atlas():
    model = AlexNet()
    model.load_graphdef()
    layer = model.layers[1]
    atlas = activation_atlas(model, layer, number_activations=subset)
    save(atlas, "tests/recipes/results/activation_atlas/atlas.jpg")


@pytest.mark.slow
def test_aligned_activation_atlas():
    model1 = AlexNet()
    model1.load_graphdef()
    layer1 = model1.layers[1]

    model2 = InceptionV1()
    model2.load_graphdef()
    layer2 = model2.layers[8]  # mixed4d

    atlasses = aligned_activation_atlas(
        model1, layer1, model2, layer2, number_activations=subset
    )
    path = f"tests/recipes/results/activation_atlas/aligned_atlas-{index}-of-{len(atlasses)}.jpg"
    for index, atlas in enumerate(atlasses):
        save(atlas, path)
