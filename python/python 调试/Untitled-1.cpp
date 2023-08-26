#include <iostream>
#include <stdlib.h>
#define LENG sizeof(LinkNode)
struct LinkNode
{
    int nData;
    LinkNode *pNext;
};
LinkNode * LinkListCreat(int nSize)
{
    LinkNode *pHead, *pTail, *pTemp;
    int nInput = 0;
    pHead = (LinkNode*)malloc(LENG);
    pTail = pHead;
    for (int i = 0; i < 3; i++)
    {
        pTemp = (LinkNode*)malloc(LENG);
        pTemp->nData = i + 1;
        pTemp->pNext = NULL;
        pTail->pNext = pTemp;
        pTail = pTail->pNext;
    }
    return pHead;
}
int GetElem(LinkNode L, int i, int& e)
{
    p = L->next;                
    int j = 1;                         
    while (p && j < i)                
        p = p->next;                
        ++j;
    }
   
    e = p->data;                    
    return OK;
}
void DestroyLinkList(LinkNode *L)
{
    LinkNode *pCur;
    pCur = L->pNext;
    if (!pCur)
    {
        free(pCur);
    }
    free(L);
}
int main(int argc, char** argv)
{
    int nListSize = 3;
    LinkNode *pList;
      pList = LinkListCreat(nListSize);
        GetElem(pList,2);
   
}
