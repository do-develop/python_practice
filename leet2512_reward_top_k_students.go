type Student struct {
    id int
    score int
}

func topStudents(positive_feedback []string, negative_feedback []string, report []string, student_id []int, k int) []int {
    positives := toSet(positive_feedback)
    negatives := toSet(negative_feedback)

    students := make([]Student, len(student_id))
    for idx, rep := range report {
        students[idx] = Student {
            id: student_id[idx],
            score: 0,
        }
        words := strings.Split(rep, " ")
        for _, word := range words {
            if _, exist := positives[word]; exist {
                students[idx].score += 3
            }
            if _, exist := negatives[word]; exist {
                students[idx].score -= 1
            }
        }
    }

    // sort the student based on score, then id
    sort.Slice(students, func(i, j int)bool {
        if students[i].score == students[j].score {
            return students[i].id < students[j].id
        }
        return students[i].score > students[j].score
    })

    topk := make([]int, 0, k)
    for i := 0; i < k; i++ {
        topk = append(topk, students[i].id)
    }
    return topk
}

func toSet(feedbacks []string)map[string]struct{} {
    feedbackSet := make(map[string] struct{})
    for _, feedback := range feedbacks {
        feedbackSet[feedback] = struct{}{}
    }
    return feedbackSet
}