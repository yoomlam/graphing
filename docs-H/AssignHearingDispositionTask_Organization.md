| [README.md](/README.md) | [Task Listing](tasklist.md) |

# AssignHearingDispositionTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after AssignHearingDispositionTask_Organization</summary>

```
digraph G {
rankdir="LR";
"HearingTask_Organization" -> "AssignHearingDispositionTask_Organization" [label=3]
}
```
</details>

![AssignHearingDispositionTask_Organization](dot/AssignHearingDispositionTask_Organization.dot.png)

**Before:**

   * [HearingTask_Organization](HearingTask_Organization.md): 3 times

**After:**


## Task Creation Sequences

### RTO.TVTO.DTO.SHTO.HTO.AHDTO

3 occurrences (example appeal IDs: [42246, 41907, 40879])

<details><summary>Task Tree for appeal with ID 42246</summary>

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
  object 3.ScheduleHearingTask #a6d854 {
Organization
}
  object 4.HearingTask #e78ac3 {
Organization
}
  object 5.AssignHearingDispositionTask #a6d854 {
Organization  <back:white>    </back>
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
4.HearingTask -- 3.ScheduleHearingTask
2.DistributionTask -- 4.HearingTask
4.HearingTask -- 5.AssignHearingDispositionTask
@enduml
```
</details>

![RTO.TVTO.DTO.SHTO.HTO.AHDTO-42246](uml/RTO.TVTO.DTO.SHTO.HTO.AHDTO-42246.png)

