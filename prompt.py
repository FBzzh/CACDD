0_shot_prompt = '你将收到一个问题和问题的答案。结合问题，将答案中的事实拆分成原子声明。一个原子声明要么表述了个体的属性，要么表述了个体与个体的关系。生成的原子声明应当是上下文独立的，请将其中的指示代词进行指代消解。输出生成的原子声明的列表。\n\n问题:{question}\n\n答案:{answer}\n\n原子声明:\n'


3_shot_prompt = {
  {'role': 'user', 'content': '你将收到一个问题和问题的答案。结合问题，将答案中的事实拆分成原子声明。一个原子声明要么表述了个体的属性，要么表述了个体与个体的关系。生成的原子声明应当是上下文独立的，请将其中的指示代词进行指代消解。输出生成的原子声明的列表。\n\n问题: 为什么有些人会沉迷于运动，而对有些人来说是一种折磨？\n\n答案:运动当中所产生的多种化学物质，是更为强有力地使人感到愉悦的方式。我们在运动中身体释放的化学物质包括——内啡肽、5-羟色胺（血清素）、多巴胺，增强愉悦感；同时会降低肾上腺素和皮质醇的激素活性，减轻焦虑和紧张感。这五种化学物质的组合拳，已被证明可以缓解焦虑和抑郁症状。因此有些人沉迷于运动是因为可以让他们感到快乐【1】而觉得运动是折磨是并没有从运动中感受到快乐。\n\n原子声明:\n'},
  {'role': 'assistant', 'content': '运动当中会产生多种化学物质。\n多种化学物质是更为强有力地使人感到愉悦的方式。\n我们在运动中身体释放的化学物质包括内啡肽。\n我们在运动中身体释放的化学物质包括5-羟色胺（血清素）。\n我们在运动中身体释放的化学物质包括多巴胺。\n内啡肽能增强愉悦感。\n5-羟色胺（血清素）能增强愉悦感。\n多巴胺能增强愉悦感。\n我们在运动中会降低肾上腺素的激素活性。\n我们在运动中会降低皮质醇的激素活性。\n降低肾上腺素的激素活性能减轻焦虑和紧张感。\n降低皮质醇的激素活性能减轻焦虑和紧张感。\n五种化学物质的组合拳，已被证明可以缓解焦虑和抑郁症状。\n有些人沉迷于运动是因为可以让他们感到快乐。\n觉得运动是折磨是并没有从运动中感受到快乐。\n'},
  {'role': 'user', 'content': '你将收到一个问题和问题的答案。结合问题，将答案中的事实拆分成原子声明。一个原子声明要么表述了个体的属性，要么表述了个体与个体的关系。生成的原子声明应当是上下文独立的，请将其中的指示代词进行指代消解。输出生成的原子声明的列表。\n\n问题: 当我们自由下落时，为什么我们开始几乎无法控制地挥舞手臂和腿？\n\n答案:1.保持平衡。2.人的一种应激反应。人受到外界的刺激，大脑、神经自然会发生条件反射，这个时候就产生一股应激的信号和能量，一定要通过肢体的动作把这种能量传导出去，手臂无疑是最灵活的肢体部分，趋利避害是人的本能，于是这就对你的大脑和神经产生刺激，你的身体必会做出应激反应。\n\n原子声明:\n'},
  {'role': 'assistant', 'content': '自由下落时无法控制地挥舞手臂和腿是保持平衡。\n自由下落时无法控制地挥舞手臂和腿是人的一种应激反应。\n人受到外界的刺激，大脑自然会发生条件反射。\n人受到外界的刺激，神经自然会发生条件反射。\n发生条件反射的时候就产生一股应激的信号和能量。\n一定要通过肢体的动作把应激的能量传导出去。\n手臂是最灵活的肢体部分。\n趋利避害是人的本能。'},
  {'role': 'user', 'content': '你将收到一个问题和问题的答案。结合问题，将答案中的事实拆分成原子声明。一个原子声明要么表述了个体的属性，要么表述了个体与个体的关系。生成的原子声明应当是上下文独立的，请将其中的指示代词进行指代消解。输出生成的原子声明的列表。\n\n问题: 犹太人为什么会受到如此多次的迫害？\n\n答案:核心原因是犹太人的特立独行，生活在其他族裔中间却坚决和他们划清界线。所以每当社会矛盾出现时这些特立独行的异族都是绝佳的出气筒和替罪羊。【1】次要原因是犹太人自己也不是很讨喜的邻居，说是讨厌鬼也不为过。犹太人从事的行业主要是商业和金融，搁古代就是奸商和放高利贷的。没有权力的庇护还总是喜欢挑大梁。【2】\n\n原子声明:\n'},
  {'role': 'assistant', 'content': '犹太人会受到如此多次的迫害核心原因是犹太人的特立独行。\n犹太人生活在其他族裔中间却坚决和他们划清界线。\n每当社会矛盾出现时这些特立独行的异族都是绝佳的出气筒和替罪羊。\n犹太人从事的行业主要是商业和金融。'},
}
