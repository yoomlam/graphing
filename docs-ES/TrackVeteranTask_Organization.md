| [README.md](/README.md) | [Task Listing](tasklist.md) |

# TrackVeteranTask_Organization

[TrackVeteranTask_Organization description](../descr/TrackVeteranTask_Organization.md)

## Tasks Created Before and After

<details><summary>Tasks created before and after TrackVeteranTask_Organization</summary>

```
digraph G {
rankdir="LR";
"TrackVeteranTask_Organization" -> "JudgeAssignTask_User" [label=2]
"RootTask_Organization" -> "TrackVeteranTask_Organization" [label=66]
"EvidenceSubmissionWindowTask_Organization" -> "TrackVeteranTask_Organization" [label=2]
"TrackVeteranTask_Organization" -> "DistributionTask_Organization" [label=66]
"TrackVeteranTask_Organization" -> "TrackVeteranTask_Organization" [label=3]
}
```
</details>

![TrackVeteranTask_Organization](dot/TrackVeteranTask_Organization.dot.png)

**Before:**

   * [RootTask_Organization](RootTask_Organization.md): 66 times
   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 3 times
   * [EvidenceSubmissionWindowTask_Organization](EvidenceSubmissionWindowTask_Organization.md): 2 times

**After:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 66 times
   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 3 times
   * [JudgeAssignTask_User](JudgeAssignTask_User.md): 2 times

## Task Creation Sequences

### RTO.TVTO

[RTO.TVTO description](../descr/RTO.TVTO.md)

66 occurrences (example appeal IDs: [40915, 42334, 41269, 42634, 40596])

<details><summary>Task Tree for appeal with ID 40915</summary>

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
Organization  <back:white>    </back>
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
2.DistributionTask -- 3.EvidenceSubmissionWindowTask
@enduml
```
</details>

![RTO.TVTO-40915](uml/RTO.TVTO-40915.png)

### RTO.TVTO.TVTO

[RTO.TVTO.TVTO description](../descr/RTO.TVTO.TVTO.md)

3 occurrences (example appeal IDs: [40894, 42805, 42609])

<details><summary>Task Tree for appeal with ID 40894</summary>

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
Organization  <back:white>    </back>
}
  object 2.TrackVeteranTask #8da0cb {
Organization  <back:white>    </back>
}
  object 3.DistributionTask #fc8d62 {
Organization
}
  object 4.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.TrackVeteranTask
0.RootTask -- 3.DistributionTask
3.DistributionTask -- 4.EvidenceSubmissionWindowTask
@enduml
```
</details>

![RTO.TVTO.TVTO-40894](uml/RTO.TVTO.TVTO-40894.png)

### RTO.DTO.ESWTO.TVTO

[RTO.DTO.ESWTO.TVTO description](../descr/RTO.DTO.ESWTO.TVTO.md)

2 occurrences (example appeal IDs: [15152, 17948])

<details><summary>Task Tree for appeal with ID 15152</summary>

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
  object 2.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
  object 3.TrackVeteranTask #8da0cb {
Organization  <back:white>    </back>
}
  object 4.JudgeAssignTask #8da0cb {
User
}
  object 5.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 6.AttorneyTask #fc8d62 {
User
}
  object 7.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 8.BvaDispatchTask #e5c494 {
Organization
}
  object 9.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.DistributionTask
1.DistributionTask -- 2.EvidenceSubmissionWindowTask
0.RootTask -- 3.TrackVeteranTask
0.RootTask -- 4.JudgeAssignTask
0.RootTask -- 5.JudgeDecisionReviewTask
5.JudgeDecisionReviewTask -- 6.AttorneyTask
0.RootTask -- 7.JudgeDecisionReviewTask
0.RootTask -- 8.BvaDispatchTask
8.BvaDispatchTask -- 9.BvaDispatchTask
@enduml
```
</details>

![RTO.DTO.ESWTO.TVTO-15152](uml/RTO.DTO.ESWTO.TVTO-15152.png)

