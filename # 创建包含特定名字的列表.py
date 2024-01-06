import thulac

def replace_entities(user_input, entities, entity_type, original_words):
    for entity in entities:
        replace = input(f"是否替换'{entity}'？ (y/n/d): ")
        if replace.lower() == 'y':
            new_entity = input(f"请输入替换'{entity}'的新{entity_type}：")
            for i, word in enumerate(original_words):
                if word == entity:
                    original_words[i] = new_entity
            user_input = " ".join(original_words)
        elif replace.lower() == 'n':
            continue
        else:
            original_words = [word for word in original_words if word != entity]
            user_input = " ".join(original_words)
    return user_input

def reorder_sentence(sentence):
    thu = thulac.thulac()
    word_tuples = thu.cut(sentence, text=False)
    reordered_sentence = " ".join([word[0] for word in word_tuples])
    return reordered_sentence

try:
    # 用户输入一段中文文字
    user_input = input("请输入一段中文文字：")

    # 使用THULAC进行分词
    thu = thulac.thulac()
    word_tuples = thu.cut(user_input, text=False)

    # 提取名词、形容词、动词、人名
    nouns = [word[0] for word in word_tuples if word[1] == 'n']
    adjectives = [word[0] for word in word_tuples if word[1] == 'a']
    verbs = [word[0] for word in word_tuples if word[1] == 'v']
    names = [word[0] for word in word_tuples if word[1] == 'np']

    # 去重，保留唯一的名词、形容词、动词、人名
    unique_nouns = list(set(nouns))
    unique_adjectives = list(set(adjectives))
    unique_verbs = list(set(verbs))
    unique_names = list(set(names))

    # 显示提取到的实体
    if unique_nouns:
        print("发现的名词:", ", ".join(unique_nouns))
    if unique_adjectives:
        print("发现的形容词:", ", ".join(unique_adjectives))
    if unique_verbs:
        print("发现的动词:", ", ".join(unique_verbs))
    if unique_names:
        print("发现的人名:", ", ".join(unique_names))

    # 保存原始的分词结果
    original_words = [word[0] for word in word_tuples]

    # 用户选择要替换的实体
    user_input = replace_entities(user_input, unique_nouns, "名词", original_words)
    user_input = replace_entities(user_input, unique_adjectives, "形容词", original_words)
    user_input = replace_entities(user_input, unique_verbs, "动词", original_words)
    user_input = replace_entities(user_input, unique_names, "人名", original_words)

    # 重新排列句子
    reordered_input = reorder_sentence(user_input)

    # 输出替换并重新排列后的结果
    print("替换并重新排列后的结果：", reordered_input)

except Exception as e:
    print(f"发生错误: {e}")
