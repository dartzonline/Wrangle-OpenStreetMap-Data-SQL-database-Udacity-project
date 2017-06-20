import csv, sqlite3

def number_of_nodes():
    result = cur.execute('SELECT COUNT(*) FROM nodes')
    return result.fetchone()[0]

def number_of_ways():
    result = cur.execute('SELECT COUNT(*) FROM ways')
    return result.fetchone()[0]

def number_of_Unique_users():
    result = cur.execute('SELECT COUNT(distinct(uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways)')
    return result.fetchone()[0]

def Top_Contributing_user():
    for row in cur.execute('SELECT e.user, COUNT(*) as num \
                            FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
                            GROUP BY e.user \
                            ORDER BY num DESC \
                            LIMIT 1'):
        return row

def Biggest_religion():
    for row in cur.execute('SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags \
                            JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="place_of_worship") i \
                            ON nodes_tags.id=i.id \
                            WHERE nodes_tags.key="religion" \
                            GROUP BY nodes_tags.value \
                            ORDER BY num DESC\
                            LIMIT 1'):
         return row

def popular_amenity():
    for row in cur.execute('SELECT value, COUNT(*) as num \
                            FROM nodes_tags \
                            WHERE key="amenity" \
                            GROUP BY value \
                            ORDER BY num DESC \
                            LIMIT 1'):
        return row

                
if __name__ == '__main__':

    con = sqlite3.connect("houston_texas.db") 
    cur = con.cursor()
    print "Number of nodes: " , number_of_nodes()
    print "Number of ways: " , number_of_ways()
    print "Number of unique users: " , number_of_Unique_users()
    print "Top Contributing user: " , Top_Contributing_user()
    print "Biggest religion: " , Biggest_religion()
    print "popular amenity: " , popular_amenity()

