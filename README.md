# Text-to-Video 모델을 활용한 공작기계 매뉴얼 영상 생성 연구
Fine-Tuning AnimateDiff framework(Text-To-Video) to optimize it for machine tool domain

## Overview
목적: 
T2V 모델을 공작기계 도메인에 최적화하여, 작업 지시 텍스트를 입력받아 해당 작업을 수행하는 가이드라인 영상을 생성하는 Text-to-video 시스템을 개발

목표:
1. 명확한 공작기계 이미지를 학습하기 위하여 이미지 도메인에서 Fine-Tuning 수행
2. 공정 과정(밀링, 터닝)의 움직임을 학습시키기 위하여 영상 도메인에서 Fine-Tuning 수행
사전 학습된 모델에 공작기계 데이터를 학습한 LoRA 파일을 적용하는 방식으로 Fine-Tuning.

## Business Understanding
1. 생성 인공지능 기술 동향
언어 모델인 GPT-4, 이미지 생성 모델인 Stable Diffusion, 그리고 동영상 생성 모델인 구글 LUMIERE 등 다양한 분야에서 혁신적인 성과 보임.

특히 OpenAI에서 공개한 영상 생성 AI 모델 'Sora'는, 이전에 공개된 다른 모델들에 비해 압도적인 퀄리티의 영상을 선보이며

영상 생성 AI 뿐만 아니라 수많은 산업군에 응용 및 적용 가능한 게임 체인저로 여겨지며, 일상 속에 전방위적인 기술 혁신을 예고하고 있다.

공개된 기술 블로그에 따르면, Sora 는 Vision Transformer(ViT), Diffusion Transformer(DiT) 등의 구조를 적용함으로써 영상 퀄리티를 크게 향상시킨 것으로 예상할 수 있다.

![wZvgUjoXojFGK7AJvMq6T7](https://github.com/kosonkh7/T2V-Machine-tool-Fine-Tuning/assets/83086978/d952c6d9-5812-4b8e-880b-8db87e9e5f68)


2. 공작기계 도메인
공작기계(Machine Tool)란, 기계를 만드는 기계(Mother Machine)이다.

기계를 만든다는 것은 기계의 부품을 만드는 것이며, 다양한 제조방법 중에서 절삭가공과 소성가공에 이용되는 모든 기계를 의미한다.

산업 현장에서 작업자들의 고령화와 외국인 인력 비중 증가하는 추세이며, 

공작기계 조작법이 담긴 매뉴얼은 방대한 내용을 담고 있어 작업자들이 숙지하기에 어려움을 겪고 있다.

알고자 하는 매뉴얼 내용을 동영상으로 바로 제시하여 편의를 제공하는 것이 프로젝트 목적이다.


## Data Understanding


## Modeling and Evaluation

## Conclusion

## Reference
