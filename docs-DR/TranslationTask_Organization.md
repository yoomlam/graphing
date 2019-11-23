| [README.md](/README.md) | [Task Listing](tasklist.md) |

# TranslationTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after TranslationTask_Organization</summary>

```
digraph G {
rankdir="LR";
"DistributionTask_Organization" -> "TranslationTask_Organization" [label=1]
}
```
</details>

![TranslationTask_Organization](dot/TranslationTask_Organization.dot.png)

**Before:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 1 times

**After:**


## Task Creation Sequences

### RTO.DTO.TTO

1 occurrences (example appeal IDs: [41094])

<details><summary>Task Tree for appeal with ID 41094</summary>

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
  object 2.TranslationTask #e5c494 {
Organization  <back:white>    </back>
}
0.RootTask -- 1.DistributionTask
1.DistributionTask -- 2.TranslationTask
@enduml
```
</details>

![RTO.DTO.TTO-41094](uml/RTO.DTO.TTO-41094.png)

