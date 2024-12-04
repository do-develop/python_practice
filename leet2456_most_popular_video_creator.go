func mostPopularCreator(creators []string, ids []string, views []int) [][]string {
    type creator string
    type id string
    type info struct {
        totalView int
        maxView int
        minId id
    }

    data := make(map[creator]info, len(creators))
    maxTotalView := 0

    for i := 0; i< len(ids); i++ {
        dt, ok := data[creator(creators[i])]
        if !ok {
            dt = info {
                totalView: views[i],
                maxView: views[i],
                minId: id(ids[i]),
            }
        } else {
            dt.totalView += views[i]
            if views[i] == dt.maxView {
                if id(ids[i]) < dt.minId {
                    dt.minId = id(ids[i])
                }
            } else if views[i] > dt.maxView {
                dt.minId = id(ids[i])
                dt.maxView = views[i]
            }
        }
        data[creator(creators[i])] = dt
        if dt.totalView > maxTotalView {
            maxTotalView = dt.totalView
        }
    }

    var result [][]string
    for crt, dt := range data {
        if dt.totalView == maxTotalView {
            result = append(result, []string{string(crt), string(dt.minId)})
        }
    }
    return result

}