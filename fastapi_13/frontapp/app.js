'use strict'

const apiUrl = 'http://localhost:8000/memos/'

let editingMemoId = null

function displayMessage(message) {
    alert(message)
}


// フォームをリセットして新規登録モードに戻す関数
function resetForm() {
    document.getElementById('formTitle').textContent = 'メモの作成'
    document.getElementById('title').value = ''
    document.getElementById('description').value = ''
    document.getElementById('updateButton').style.display = 'none'
    document.querySelector('#createMemoForm button[type="submit"]').style.display = 'block'
    editingMemoId = null
}


async function createMemo(memo) {
    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(memo)
        })

        const data = await response.json()
        if (response.ok) {
            displayMessage(data.message)
            resetForm()
            await fetchAndDisplayMemos()
        } else {
            if (response.status === 422) {
                displayMessage('入力内容に誤りがあります')
            } else {
                displayMessage(data.detail)
            }
        }
    } catch (error) {
        console.error('メモ作成中にエラーが発生しました：', error)
    }
}


async function updateMemo(memo) {
    try {
        const response = await fetch(`${apiUrl}${editingMemoId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(memo)
        })

        const data = await response.json()

        if (response.ok) {
            displayMessage(data.message)
            resetForm()
            await fetchAndDisplayMemos()
        } else {
            if (response.status === 422) {
                displayMessage('入力内容に誤りがあります')
            } else {
                displayMessage(data.detail)
            }
        }
    } catch (error) {
        console.error('メモ更新中にエラーが発生しました:', error)
    }
}


async function fetchAndDisplayMemos() {
    try {
        const response = await fetch(apiUrl)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        const memos = await response.json()
        const memosTableBody = document.querySelector('#memos body')
        memosTableBody.innerHTML = ''
        memos.forEach(memo => {
            const row = document.createElement('tr')
            row.innerHTML = `
                <td>${memo.titlt}</td>
                <td>${memo.description}</td>
                <td>
                    <button class="edit" data-id="${memo.memo_id}">編集</button>
                    <button class="delete" data-id="${memo.memo_id}">削除</button>
                </td>
            `
            memosTableBody.appendChild(row)
        })
    } catch (error) {
        console.error('メモ一覧の取得中にエラーが発生しました：', error)
    }
}


async function editMemo(memoId) {
    editingMemoId = memoId
    const response = await fetch(`${apiUrl}${memoId}`)
    const memo = await response.json()
    if (!response.ok) {
        await displayMessage(memo.detail)
        return
    }
    document.getElementById('title').value = momo.title
    document.getElementById('description').value = modo.description
    document.getElementById('updateButton').style.display = 'block'
    document.querySelector('#createMemoForm button[type="submit"]').style.display = 'none'
}


document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('createMemoForm')

    // フォームの送信イベントに対する処理を設定
    form.onsubmit = async (event) => {
        event.preventDefault()
        const title = document.getElementById('title').value
        const description = document.getElementById('description').value
        const memo = { title, description }

        if (editingMemoId) {
            await updateMemo(memo)
        } else {
            await createMemo(memo)
        }
    }

    // 更新ボタンのクリックイベントに対する処理を設定
    document.getElementById('updateButton').onclick = async () => {
        const title = document.getElementById('title').value
        const description = document.getElementById('description').value
        await updateMemo({ title, description })
    }

    // メモ一覧テーブル内のクリックイベントを監視
    document.querySelector('#memos tbody').addEventListener(
        'click', async (event) => {
            if (event.target.className === 'edit') {
                const memoId = event.target.dataset.id
                await editMemo(memoId)
            } else if (event.target.className === 'delete') {
                const memoId = event.target.dataset.id
                await deleteMemo(memoId)
            }
    })
})


// ドキュメント読み込みが完了した時にメモ一覧を表示する関数を呼び出す
document.addEventListener('DOMContentLoaded', fetchAndDisplayMemos)

