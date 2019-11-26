| [README.md](/README.md) | [Task Listing](tasklist.md) |

# JudgeAssignTask_User

[JudgeAssignTask_User description](../descr/JudgeAssignTask_User.md)

## Tasks Created Before and After

<details><summary>Tasks created before and after JudgeAssignTask_User</summary>

```
digraph G {
rankdir="LR";
"TrackVeteranTask_Organization" -> "JudgeAssignTask_User" [label=1]
"InformalHearingPresentationTask_Organization" -> "JudgeAssignTask_User" [label=6]
"DistributionTask_Organization" -> "JudgeAssignTask_User" [label=16]
"InformalHearingPresentationTask_User" -> "JudgeAssignTask_User" [label=4]
"EvidenceOrArgumentMailTask_User" -> "JudgeAssignTask_User" [label=1]
"SpecialCaseMovementTask_User" -> "JudgeAssignTask_User" [label=1]
"JudgeAssignTask_User" -> "IhpColocatedTask_Organization" [label=1]
"JudgeAssignTask_User" -> "JudgeDecisionReviewTask_User" [label=21]
}
```
</details>

![JudgeAssignTask_User](dot/JudgeAssignTask_User.dot.png)

**Before:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 16 times
   * [InformalHearingPresentationTask_Organization](InformalHearingPresentationTask_Organization.md): 6 times
   * [InformalHearingPresentationTask_User](InformalHearingPresentationTask_User.md): 4 times
   * [EvidenceOrArgumentMailTask_User](EvidenceOrArgumentMailTask_User.md): 1 times
   * [SpecialCaseMovementTask_User](SpecialCaseMovementTask_User.md): 1 times
   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 1 times

**After:**

   * [JudgeDecisionReviewTask_User](JudgeDecisionReviewTask_User.md): 21 times
   * [IhpColocatedTask_Organization](IhpColocatedTask_Organization.md): 1 times

## Task Creation Sequences

### RTO.DTO.JATU

[RTO.DTO.JATU description](../descr/RTO.DTO.JATU.md)

8 occurrences (example appeal IDs: [32724, 38039, 40828, 3875, 40611])

<details><summary>Task Tree for appeal with ID 32724</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.DistributionTask #fc8d62 {
Organization
}
  object 2.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 3.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 4.AttorneyTask #fc8d62 {
User
}
  object 5.BvaDispatchTask #e5c494 {
Organization
}
  object 6.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.DistributionTask
0.RootTask -- 2.JudgeAssignTask
0.RootTask -- 3.JudgeDecisionReviewTask
3.JudgeDecisionReviewTask -- 4.AttorneyTask
0.RootTask -- 5.BvaDispatchTask
5.BvaDispatchTask -- 6.BvaDispatchTask
@enduml
```
</details>

![RTO.DTO.JATU-32724](uml/RTO.DTO.JATU-32724.png)

### RTO.TVTO.DTO.JATU

[RTO.TVTO.DTO.JATU description](../descr/RTO.TVTO.DTO.JATU.md)

6 occurrences (example appeal IDs: [40595, 33346, 41369, 37901, 40892])

<details><summary>Task Tree for appeal with ID 40595</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.TrackVeteranTask #8da0cb {
Organization
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 4.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 5.AttorneyTask #fc8d62 {
User
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
0.RootTask -- 3.JudgeAssignTask
0.RootTask -- 4.JudgeDecisionReviewTask
4.JudgeDecisionReviewTask -- 5.AttorneyTask
@enduml
```
</details>

![RTO.TVTO.DTO.JATU-40595](uml/RTO.TVTO.DTO.JATU-40595.png)

### RTO.TVTO.DTO.IHPTO.JATU

[RTO.TVTO.DTO.IHPTO.JATU description](../descr/RTO.TVTO.DTO.IHPTO.JATU.md)

6 occurrences (example appeal IDs: [34538, 39812, 10197, 39823, 7729])

<details><summary>Task Tree for appeal with ID 34538</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.TrackVeteranTask #8da0cb {
Organization
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.InformalHearingPresentationTask #ffd92f {
Organization
}
  object 4.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 5.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 6.AttorneyTask #fc8d62 {
User
}
  object 7.BvaDispatchTask #e5c494 {
Organization
}
  object 8.BvaDispatchTask #e5c494 {
User
}
  object 9.BvaDispatchTask #e5c494 {
User
}
  object 10.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
2.DistributionTask -- 3.InformalHearingPresentationTask
0.RootTask -- 4.JudgeAssignTask
0.RootTask -- 5.JudgeDecisionReviewTask
5.JudgeDecisionReviewTask -- 6.AttorneyTask
0.RootTask -- 7.BvaDispatchTask
7.BvaDispatchTask -- 8.BvaDispatchTask
7.BvaDispatchTask -- 9.BvaDispatchTask
7.BvaDispatchTask -- 10.BvaDispatchTask
@enduml
```
</details>

![RTO.TVTO.DTO.IHPTO.JATU-34538](uml/RTO.TVTO.DTO.IHPTO.JATU-34538.png)

### RTO.TVTO.DTO.IHPTO.IHPTU.JATU

[RTO.TVTO.DTO.IHPTO.IHPTU.JATU description](../descr/RTO.TVTO.DTO.IHPTO.IHPTU.JATU.md)

4 occurrences (example appeal IDs: [30234, 35142, 5529, 34472])

<details><summary>Task Tree for appeal with ID 30234</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.TrackVeteranTask #8da0cb {
Organization
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.InformalHearingPresentationTask #ffd92f {
Organization
}
  object 4.InformalHearingPresentationTask #ffd92f {
User
}
  object 5.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 6.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 7.AttorneyTask #fc8d62 {
User
}
  object 8.BvaDispatchTask #e5c494 {
Organization
}
  object 9.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
2.DistributionTask -- 3.InformalHearingPresentationTask
3.InformalHearingPresentationTask -- 4.InformalHearingPresentationTask
0.RootTask -- 5.JudgeAssignTask
0.RootTask -- 6.JudgeDecisionReviewTask
6.JudgeDecisionReviewTask -- 7.AttorneyTask
0.RootTask -- 8.BvaDispatchTask
8.BvaDispatchTask -- 9.BvaDispatchTask
@enduml
```
</details>

![RTO.TVTO.DTO.IHPTO.IHPTU.JATU-30234](uml/RTO.TVTO.DTO.IHPTO.IHPTU.JATU-30234.png)

### DTO.JATU

[DTO.JATU description](../descr/DTO.JATU.md)

2 occurrences (example appeal IDs: [6702, 10958])

<details><summary>Task Tree for appeal with ID 6702</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.TrackVeteranTask #8da0cb {
Organization
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 4.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 5.AttorneyTask #fc8d62 {
User
}
  object 6.OtherColocatedTask #66c2a5 {
Organization
}
  object 7.OtherColocatedTask #66c2a5 {
User
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
0.RootTask -- 3.JudgeAssignTask
0.RootTask -- 4.JudgeDecisionReviewTask
4.JudgeDecisionReviewTask -- 5.AttorneyTask
5.AttorneyTask -- 6.OtherColocatedTask
6.OtherColocatedTask -- 7.OtherColocatedTask
@enduml
```
</details>

![DTO.JATU-6702](uml/DTO.JATU-6702.png)

### RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU

[RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU description](../descr/RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU.md)

1 occurrences (example appeal IDs: [10213])

<details><summary>Task Tree for appeal with ID 10213</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.DistributionTask #fc8d62 {
Organization
}
  object 2.EvidenceOrArgumentMailTask #ffd92f {
Organization
}
  object 3.EvidenceOrArgumentMailTask #ffd92f {
Organization
}
  object 4.EvidenceOrArgumentMailTask #ffd92f {
User
}
  object 5.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 6.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 7.AttorneyTask #fc8d62 {
User
}
  object 8.BvaDispatchTask #e5c494 {
Organization
}
  object 9.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.DistributionTask
0.RootTask -- 2.EvidenceOrArgumentMailTask
2.EvidenceOrArgumentMailTask -- 3.EvidenceOrArgumentMailTask
3.EvidenceOrArgumentMailTask -- 4.EvidenceOrArgumentMailTask
0.RootTask -- 5.JudgeAssignTask
0.RootTask -- 6.JudgeDecisionReviewTask
6.JudgeDecisionReviewTask -- 7.AttorneyTask
0.RootTask -- 8.BvaDispatchTask
8.BvaDispatchTask -- 9.BvaDispatchTask
@enduml
```
</details>

![RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU-10213](uml/RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU-10213.png)

### RTO.DTO.SCMTU.JATU

[RTO.DTO.SCMTU.JATU description](../descr/RTO.DTO.SCMTU.JATU.md)

1 occurrences (example appeal IDs: [41963])

<details><summary>Task Tree for appeal with ID 41963</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.DistributionTask #fc8d62 {
Organization
}
  object 2.SpecialCaseMovementTask #66c2a5 {
User
}
  object 3.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
0.RootTask -- 1.DistributionTask
1.DistributionTask -- 2.SpecialCaseMovementTask
0.RootTask -- 3.JudgeAssignTask
@enduml
```
</details>

![RTO.DTO.SCMTU.JATU-41963](uml/RTO.DTO.SCMTU.JATU-41963.png)

### RTO.DTO.TVTO.JATU

[RTO.DTO.TVTO.JATU description](../descr/RTO.DTO.TVTO.JATU.md)

1 occurrences (example appeal IDs: [11092])

<details><summary>Task Tree for appeal with ID 11092</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.DistributionTask #fc8d62 {
Organization
}
  object 2.TrackVeteranTask #8da0cb {
Organization
}
  object 3.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 4.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 5.AttorneyTask #fc8d62 {
User
}
0.RootTask -- 1.DistributionTask
0.RootTask -- 2.TrackVeteranTask
0.RootTask -- 3.JudgeAssignTask
0.RootTask -- 4.JudgeDecisionReviewTask
4.JudgeDecisionReviewTask -- 5.AttorneyTask
@enduml
```
</details>

![RTO.DTO.TVTO.JATU-11092](uml/RTO.DTO.TVTO.JATU-11092.png)

