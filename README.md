# Text-to-Video 모델을 활용한 공작기계 매뉴얼 영상 생성 연구
## Overview
**목적:** <br>
T2V 모델을 공작기계 도메인에 최적화하여, <br>
작업 지시 텍스트를 입력받아 해당 작업을 수행하는 가이드라인 영상을 생성하는 Text-to-video 시스템을 개발<br>

**목표:**
1. 명확한 공작기계 이미지를 학습하기 위하여 이미지 도메인에서 Fine-Tuning 수행
2. 공정 과정(밀링, 터닝)의 움직임을 학습시키기 위하여 영상 도메인에서 Fine-Tuning 수행<br>

사전 학습된 모델에 공작기계 데이터를 학습한 LoRA 파일을 적용하는 방식으로 Fine-Tuning.

## Business Understanding
### 생성 인공지능 기술 동향

언어 모델인 GPT-4, 이미지 생성 모델인 Stable Diffusion, 그리고 동영상 생성 모델인 구글 LUMIERE 등 다양한 분야에서 혁신적인 성과 보임.

특히 OpenAI에서 공개한 영상 생성 AI 모델 'Sora'는, 이전에 공개된 다른 모델들에 비해 압도적인 퀄리티의 영상을 선보이며

수많은 산업군에 응용 및 적용 가능한 게임 체인저로 여겨지며, 일상에 전방위적인 기술 혁신을 예고하고 있다.

공개된 기술 블로그에 따르면, Sora 는 Vision Transformer(ViT), Diffusion Transformer(DiT) 등의 구조를 적용함으로써 영상 퀄리티를 크게 향상시킨 것으로 예상할 수 있다.

![wZvgUjoXojFGK7AJvMq6T7](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/d952c6d9-5812-4b8e-880b-8db87e9e5f68)

### 공작기계 도메인

공작기계(Machine Tool)란, 기계를 만드는 기계(Mother Machine)이다.

산업 현장에서 작업자들의 고령화와 외국인 인력 비중 증가하는 추세이며, 

공작기계 조작법이 담긴 매뉴얼은 방대한 내용을 담고 있어 작업자들이 숙지하기에 어려움을 겪고 있다.

알고자 하는 매뉴얼 내용을 동영상으로 바로 제시하여 편의를 제공하는 것이 프로젝트 목적이다.

### 밀링, 터닝

밀링 공정: 공작물이 고정된 상태에서 절삭 공구가 여러 축을 따라 이동하며 고속으로 회전한다.<br>
터닝 공정: 절삭 공구가 고정되어 있고 스핀들이 공작물을 회전시킨다.


## Preliminaries
### Stable Diffusion (SD)
![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/7f5c5b16-6b8f-4c4f-8b8f-5b8b20346989)

Latent Diffusion model(LDM)이라고도 불리며, 고해상도 이미지를 잠재 공간(Latent Space)을 활용하여 효율적으로 생성하는 대표적인 Text-to-Image(T2I) 모델이다. SD 학습 과정에 대해서 간략하게 설명하면 다음과 같다.

1. 고해상도의 입력 이미지에 대해서 사전 학습된 VQ-GAN 혹은 VQ-VAE와 같은 AutoEncoder를 통해 정보가 압축된 잠재 공간을 생성한다.
2. Forward Process: 잠재 공간에 대해서 Markov Process 기반 노이즈 생성한다. 이를 확산 과정이라고 한다.
3. Conditioning Mechanism: 텍스트 정보가 담긴 프롬프트를 CLIP VIT-L/14 text encoder를 통해 이미지와 같은 차원의 Sequence Vector로 임베딩한다.
4. Reverse Process: 잠재 공간으로부터 U-Net 구조를 보이는 디노이즈 과정을 수행한다. 본 구조는 ResNet, Spatial Self-Attention layers, Cross-Attention layer를 포함하며, 이 과정에서 이미지와 프롬프트 간의 상관관계를 반영하여 이미지 정보에 반영한다.

### Low-rank adaptation (LoRA)
![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/b76c0f6d-84d0-4cb3-97d2-2f7f16769d70)

LoRA는 Large Language Model(LLM)을 비용 효율적으로 최적화하기 위해 제안된 방법론이다. <br>
LoRA는 주로 Attention layer에 적용되며, layer에 Rank-Decomposition matrix를 더해주는데, 이는 사전 학습된 모델의 가중치는 고정한 채로 Residual만 Fine-Tuning하여 더해주는 것을 의미한다. <br>
따라서 전체 모델 가중치를 다시 학습하는 것보다 연산량과 연산 시간을 절감하여 Fine-Tuning 할 수 있다.<br>

### AnimateDiff
AnimateDiff는 사전 학습된 T2I 모델에 motion module을 적용하여 영상을 생성할 수 있는 Text-to-Video(T2V) 프레임워크이다. 학습 과정에 대해 간략하게 설명하면 다음과 같다.
![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/355ba493-c2cb-4b97-bcee-8dc028271683)

1. Domain Adapter: 일반적으로 이미지 데이터에 비해 영상 데이터의 품질이 떨어지기 때문에, Domain Adapter를 적용하여 T2I 모델의 사전 학습 이미지 데이터와, 영상 학습 데이터 간의 시각적 특징 차이로 인해 발생할 수 있는 부정적인 영향을 완화한다. domain adapter는 T2I의 Cross-Attention layer에 적용된다. <br>
 ![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/03d47f95-94f4-4c21-9ece-c85fa3c511c6)

2. Network Inflation: 사전학습된 이미지 레이어의 구조를 5D video tensor로 변환하여 영상의 시간 정보를 담을 수 있도록 수정한다.<br>
3. Motion Module Design: 움직임을 학습하기 위해 temporal Transformer를 사용한다. sinusoidal position encoding을 통해 영상에서 각 프레임의 위치를 인코딩한 뒤, 시간 축을 따라 여러 개의 Self-Attention 연산을 수행하며 움직임을 학습한다.<br>


## Modeling and Evaluation
![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/b9a64368-f671-4a1b-8b17-de5ac8fdf74f)

본 프로젝트에서 T2V 모델을 공작기계 도메인에 최적화하기 위하여, <br>

명확한 공작기계 이미지를 학습하기 위한 T2I 모델 Fine-Tuning과, <br>

공작 기계의 움직임을 학습시키기 위한 Motion Module Fine-Tuning 각각 수행함으로써 보다 분명한 영상 가이드를 생성하는 것을 목표한다.

### 1. T2I 모델 Fine-Tuning
![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/0f9ecddf-1971-4b29-91d5-2ccef8131e90)

![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/97d0666b-a76f-42d3-8741-390edc0fea34)

### 2. Motion Module Fine-Tuning

![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/bcf5c6ff-d6e8-44e3-8acf-a775206bda05)

![image](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/b7544d9d-2878-4bf0-b436-e3bc0c988ba4)


## Conclusion

<a href="https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/381717fe-d4c6-4258-bd0b-953913e674ad">
    <img src="https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/381717fe-d4c6-4258-bd0b-953913e674ad" alt="밀링 결과 영상" width="400" height="400">
</a>

<a href="https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/4d9839f5-f955-40f8-a5af-24fce3012004">
    <img src="https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/4d9839f5-f955-40f8-a5af-24fce3012004" alt="터닝 결과 영상" width="400" height="400">
</a>


밀링 공정 생성 영상 결과물 (좌), 밀링 공정 생성 영상 결과물 (우) 

본 프로젝트는 AnimateDiff 프레임워크를 Fine-Tuning하여 Milling 공정과 Turning 공정을 텍스트로부터 성공적으로 구현.<br>

이는 공작기계의 가장 핵심적인 공정들을 먼저 다룬 것으로, 다양한 공정 영상 학습을 통해 현재 공작기계 산업을 이끄는 머시닝 센터(복합가공기)의 모든 공정을 반영하는 모델 개발 가능 할 것이다.<br>

현재 공작기계 산업을 이끄는 DN솔루션즈, 한화정밀기계 등, 국내 다양한 기업과의 협업을 통해, 특정 기계의 영상과 이미지 데이터 학습한다면 더 좋은 결과를 얻을 것으로 기대한다.<br>


## Reference

[Sora](https://openai.com/index/video-generation-models-as-world-simulators/)<br>
[Stable Diffusion](https://arxiv.org/abs/2112.10752)<br>
[LoRA](https://arxiv.org/abs/2106.09685)<br>
[AnimateDiff](https://arxiv.org/abs/2307.04725)<br>
[MotionDirector](https://arxiv.org/abs/2310.08465)<br>
[AnimateDiff-MotionDirector](https://github.com/ExponentialML/AnimateDiff-MotionDirector)<br>
