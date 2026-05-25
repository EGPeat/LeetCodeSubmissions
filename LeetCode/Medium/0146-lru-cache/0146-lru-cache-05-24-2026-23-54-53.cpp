struct Node{
    int key;
    int value;
    Node* prev;
    Node* next;

    Node() : key(0), value(0), prev(nullptr), next(nullptr) {}

    Node(int key, int val, Node* p, Node* n)
        : key(key), value(val), prev(p), next(n) {}
};

class LRUCache {
public:
    int cap;
    int current = 0;
    unordered_map<int, Node*> dict;
    Node head = Node(-1, -1,nullptr,nullptr);
    Node tail = Node(-2, -2,nullptr,nullptr);
    LRUCache(int capacity) {cap = capacity;head.next = &tail;
    tail.prev = &head;}
    
    int get(int key) {        
        if (dict.contains(key)){
            _remove_from_stream(dict.find(key)->second);
            _move_to_front(dict.find(key)->second);
            return dict.find(key)->second->value;
        }
        else{
            return -1;
        }
    }
    
    void put(int key, int value) {
        if (dict.contains(key)){
            dict.find(key)->second->value = value;
            _remove_from_stream(dict.find(key)->second);
            _move_to_front(dict.find(key)->second);
        }
        else{
            Node* new_node = new Node(key, value, nullptr, nullptr);
            dict[key] = new_node;
            _move_to_front(new_node);
            current += 1;
            if (current > cap){
                Node* current_node = tail.prev;
                _remove_from_stream(dict.find(current_node->key)->second);
                dict.erase(current_node->key);
                current -= 1;
            }
        }


    }

    void _move_to_front(Node* new_node){
        
        new_node->next = head.next;
        head.next->prev = new_node;

        head.next = new_node;
        new_node->prev = &head;
        

    }
    void _remove_from_stream(Node* new_node){
        new_node->prev->next = new_node->next;
        new_node->next->prev = new_node->prev;

    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */