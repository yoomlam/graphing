| [README.md](/README.md) | [Task Listing](tasklist.md) |

# RootTask_Organization

[RootTask_Organization description](../descr/RootTask_Organization.md)

## Tasks Created Before and After

<details><summary>Tasks created before and after RootTask_Organization</summary>

```
digraph G {
rankdir="LR";
"RootTask_Organization" -> "DistributionTask_Organization" [label=37]
"RootTask_Organization" -> "TrackVeteranTask_Organization" [label=66]
}
```
</details>

![RootTask_Organization](dot/RootTask_Organization.dot.png)

**Before:**


**After:**

   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 66 times
   * [DistributionTask_Organization](DistributionTask_Organization.md): 37 times

## Task Creation Sequences

### RTO

[RTO description](../descr/RTO.md)

103 occurrences (example appeal IDs: [15152, 40915, 42334, 41269, 42078])

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
Organization  <back:white>    </back>
}
  object 1.DistributionTask #fc8d62 {
Organization
}
  object 2.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
  object 3.TrackVeteranTask #8da0cb {
Organization
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

![RTO-15152](uml/RTO-15152.png)

