# HearingTask_Organization

<details><summary>Links for HearingTask_Organization</summary>

```
digraph G {
rankdir="LR";
"HearingTask_Organization" -> "AssignHearingDispositionTask_Organization" [label=3]
"HearingTask_Organization" -> "HearingAdminActionVerifyAddressTask_Organization" [label=3]
"HearingTask_Organization" -> "TrackVeteranTask_Organization" [label=1]
"HearingTask_Organization" -> "TranslationTask_Organization" [label=1]
"HearingTask_Organization" -> "ReturnedUndeliverableCorrespondenceMailTask_Organization" [label=1]
"ScheduleHearingTask_Organization" -> "HearingTask_Organization" [label=128]
}
```
</details>

![RTO.DTO.SHTO-41136](dot/RTO.DTO.SHTO.dot.png)

## Nextlinks

   * 3 [AssignHearingDispositionTask_Organization](AssignHearingDispositionTask_Organization.md)
   * 3 [HearingAdminActionVerifyAddressTask_Organization](HearingAdminActionVerifyAddressTask_Organization.md)
   * 1 [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md)
   * 1 [TranslationTask_Organization](TranslationTask_Organization.md)
   * 1 [ReturnedUndeliverableCorrespondenceMailTask_Organization](ReturnedUndeliverableCorrespondenceMailTask_Organization.md)

## Backlinks

   * 128 [ScheduleHearingTask_Organization](ScheduleHearingTask_Organization.md)

## RTO.TVTO.DTO.SHTO.HTO

119 occurrences (example appeals: [42769, 42820, 42010, 42071, 39818])

<details><summary>PlantUML for 42769</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.ScheduleHearingTask_Organization #a6d854
object 4.HearingTask_Organization #e78ac3
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
4.HearingTask_Organization -- 3.ScheduleHearingTask_Organization
2.DistributionTask_Organization -- 4.HearingTask_Organization
@enduml
```
</details>

![RTO.TVTO.DTO.SHTO.HTO-42769](uml/RTO.TVTO.DTO.SHTO.HTO-42769.png)

## RTO.DTO.SHTO.HTO

9 occurrences (example appeals: [41136, 42097, 4988, 42691, 40835])

<details><summary>PlantUML for 41136</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.ScheduleHearingTask_Organization #a6d854
object 3.HearingTask_Organization #e78ac3
0.RootTask_Organization -- 1.DistributionTask_Organization
3.HearingTask_Organization -- 2.ScheduleHearingTask_Organization
1.DistributionTask_Organization -- 3.HearingTask_Organization
@enduml
```
</details>

![RTO.DTO.SHTO.HTO-41136](uml/RTO.DTO.SHTO.HTO-41136.png)

