type Person struct {
    name string
    height int
}

func sortPeople(names []string, heights []int) []string {
    var people []Person
    for i := 0; i < len(heights); i++ {
        var p Person
        p.name = names[i]
        p.height = heights[i]
        people = append(people, p)
    }    

    sort.Slice(people, func(i, j int) bool {
        return people[i].height > people[j].height
    })

    for i, p := range(people){
        names[i] = p.name
    }
    return names
}