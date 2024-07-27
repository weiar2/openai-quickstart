import gradio as gr

from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate

from utils import ArgumentParser


def initialize_animations_bot(vector_store_dir: str="real_estates_animation"):
    db = FAISS.load_local(vector_store_dir, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

    prompt_template = """Use the following pieces of context to answer the question at the end.
        {context}
        Question: 根据下面的 description: {question}，最相似的动画片是什么？并给出评价
        Answer:"""
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": prompt}

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=args.temperature)

    global ANIMATIONS_BOT
    ANIMATIONS_BOT = RetrievalQA.from_chain_type(llm,
                                                 retriever=db.as_retriever(search_type="similarity_score_threshold",
                                                                           search_kwargs={"score_threshold": 0.7}),
                                                 chain_type_kwargs=chain_type_kwargs)
    # 返回向量数据库的检索结果
    ANIMATIONS_BOT.return_source_documents = True

    return ANIMATIONS_BOT

def animations_chat(message, history):
    print(f"[message]{message}")
    print(f"[history]{history}")

    enable_chat = args.enable_chat

    ans = ANIMATIONS_BOT({"query": message})
    # 如果检索出结果，或者开了大模型聊天模式
    # 返回 RetrievalQA combine_documents_chain 整合的结果
    if ans["source_documents"] or enable_chat:
        print(f"[result]{ans['result']}")
        print(f"[source_documents]{ans['source_documents']}")
        return ans["result"]
    # 否则输出套路话术
    else:
        return "这个问题我不知道"
    

def launch_gradio():
    demo = gr.ChatInterface(
        fn=animations_chat,
        title="Animation Search",
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="0.0.0.0")


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    print(args)

    # 初始化 Animation Search 机器人
    initialize_animations_bot()
    # 启动 Gradio 服务
    launch_gradio()
