import satlaspretrain_models
import torch

from torchgeo.trainers import SemanticSegmentationTask


class SatlasSegmentationModel(torch.nn.Module):
    def __init__(self, model_identifier, fpn, num_classes):
        super().__init__()
        weights_manager = satlaspretrain_models.Weights()
        self.model = weights_manager.get_pretrained_model(
            model_identifier=model_identifier,
            fpn=fpn,
        )
        self.head = torch.nn.Sequential(
            torch.nn.Conv2d(128, 128, 3, padding=1),
            torch.nn.ReLU(inplace=True),
            torch.nn.Conv2d(128, num_classes, 3, padding=1),
        )

    def forward(self, x):
        feature_maps = self.model(x)
        assert len(feature_maps) == 5 # 1 upsampled at beginning + 4 FPN from before the upsampling
        return self.head(feature_maps[0])


class SatlasSemanticSegmentationTask(SemanticSegmentationTask):
    def __init__(self, model_identifier: str, fpn: bool = True, pretrained: bool = True, *args, **kwargs):
        self.model_identifier = model_identifier
        self.pretrained = pretrained
        self.fpn = fpn
        super().__init__(*args, **kwargs)

    def configure_models(self):
        self.model = SatlasSegmentationModel(self.model_identifier, self.fpn, self.hparams["num_classes"])

        if self.hparams["freeze_backbone"]:
            for param in self.model.model.backbone.parameters():
                param.requires_grad = False
